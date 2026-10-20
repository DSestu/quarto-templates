"""Render marimo (.py) and Jupyter (.ipynb) notebooks with the dsestu Quarto templates.

Nothing is executed: marimo notebooks are rendered from the outputs the marimo editor
saved in __marimo__/session/, and .ipynb files from their stored outputs.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).parent
# Wheels bundle the extensions next to this file; a source checkout has them at the repo root.
EXTENSIONS = next(p for p in (HERE / "_extensions", HERE.parents[1] / "_extensions") if p.is_dir())
MARIMO_BUNDLE = "application/vnd.marimo+mimebundle"
# marimo tags the extension's marimo-outputs.html can draw without a kernel; anything else falls back to marimo's PNG snapshot
STATIC_TAGS = {"marimo-ui-element", "marimo-plotly", "marimo-table"}
AUTORUN_HINT = (
    "marimo only saves outputs when autorun on startup is off. Add this to the project's pyproject.toml\n"
    "(or set Settings > Runtime > On startup to 'lazy'), then run the notebook once in the editor:\n\n"
    "    [tool.marimo.runtime]\n    auto_instantiate = false\n"
)


class RenderError(Exception):
    pass


def session_file(notebook: Path) -> Path:
    return notebook.parent / "__marimo__" / "session" / f"{notebook.name}.json"


def front_matter(source: str) -> str | None:
    """YAML from a `# ---` ... `# ---` comment block above `import marimo`."""
    header = source.split("import marimo", 1)[0]
    m = re.search(r"^# ---[ \t]*\n(.*?)^# ---[ \t]*$", header, re.M | re.S)
    if not m:
        return None
    return "\n".join(re.sub(r"^# ?", "", line) for line in m[1].splitlines())


def _strip_data_uri(value: str) -> str:
    return value.split(",", 1)[1] if value.startswith("data:") else value


def pick_data(data: dict) -> dict:
    """Choose the ipynb mime bundle for one marimo output, preferring what stays interactive."""
    vega = next((k for k in data if k.startswith("application/vnd.vegalite")), None)
    if vega:
        spec = data[vega] if isinstance(data[vega], str) else json.dumps(data[vega])
        return {"text/html": f"<dsestu-vega data-spec='{html.escape(spec)}'></dsestu-vega>"}
    page = data.get("text/html")
    if page is not None:
        tags = set(re.findall(r"<(marimo-[\w-]+)", page))
        lazy_table = "marimo-table" in tags and "data-data='&quot;[" not in page
        if (tags <= STATIC_TAGS and not lazy_table) or "image/png" not in data:
            return {"text/html": page}
        return {"image/png": _strip_data_uri(data["image/png"])}
    return {k: _strip_data_uri(v) if k.startswith("image/") else v for k, v in data.items()}


def to_ipynb_outputs(cell: dict) -> list[dict]:
    outputs = []
    for out in cell.get("outputs", []):
        if out.get("type") == "error":
            outputs.append({"output_type": "error", "ename": out.get("ename", ""), "evalue": out.get("evalue", ""), "traceback": []})
            continue
        data = out.get("data", {})
        if MARIMO_BUNDLE in data:
            bundle = data[MARIMO_BUNDLE]
            data = json.loads(bundle) if isinstance(bundle, str) else bundle
        data = {k: v for k, v in data.items() if not k.startswith("__") and v not in ("", None)}
        if data:
            outputs.append({"output_type": "display_data", "data": pick_data(data), "metadata": {}})
    for line in cell.get("console", []):
        if line.get("type") == "stream" and line.get("mimetype", "text/plain") == "text/plain":
            outputs.append({"output_type": "stream", "name": line.get("name", "stdout"), "text": line.get("text", "")})
    return outputs


def marimo_to_ipynb(notebook: Path, workdir: Path) -> dict:
    cache = session_file(notebook)
    if not cache.exists():
        raise RenderError(f"no saved outputs for {notebook.name} ({cache} is missing).\n{AUTORUN_HINT}")
    session = json.loads(cache.read_text(encoding="utf-8"))
    if session.get("version") != "1":
        raise RenderError(f"unsupported marimo session format {session.get('version')!r} in {cache}")

    # Parses the notebook into cells; nothing runs without --include-outputs.
    exported = workdir / "cells.ipynb"
    cmd = [sys.executable, "-m", "marimo", "export", "ipynb", str(notebook), "--sort", "top-down", "-f", "-o", str(exported)]
    done = subprocess.run(cmd, capture_output=True, text=True)
    if done.returncode != 0:
        raise RenderError(f"marimo could not read {notebook.name}:\n{done.stderr or done.stdout}")
    nb = json.loads(exported.read_text(encoding="utf-8"))

    # marimo matches saved outputs to cells by code hash, since cell ids change between sessions.
    saved = {c.get("code_hash"): c for c in session.get("cells", [])}
    stale = 0
    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue
        code = "".join(cell["source"])
        match = saved.get(hashlib.md5(code.encode("utf-8")).hexdigest()) if code.strip() else None
        if match is None:
            stale += code.strip() != ""
            continue
        cell["outputs"] = to_ipynb_outputs(match)
    if stale:
        print(f"warning: {stale} cell(s) of {notebook.name} have no saved output; run them in marimo", file=sys.stderr)

    meta = front_matter(notebook.read_text(encoding="utf-8"))
    if meta:
        # Quarto only treats a raw cell as front matter when its source is a list of lines
        source = f"---\n{meta}\n---\n".splitlines(keepends=True)
        nb["cells"].insert(0, {"cell_type": "raw", "metadata": {}, "source": source})
    return nb


def render(source: Path, output: Path, fmt: str, quarto_args: list[str]) -> None:
    if shutil.which("quarto") is None:
        raise RenderError("quarto is not on PATH; install it from https://quarto.org")
    # A throwaway project: bundled extensions, no execution, and no clash with a same-named .py next to the source.
    with tempfile.TemporaryDirectory(prefix="dsestu-render-") as tmp:
        tmp = Path(tmp)
        shutil.copytree(EXTENSIONS, tmp / "_extensions")
        (tmp / "_quarto.yml").write_text(
            "project:\n  type: default\nexecute:\n  enabled: false\n"
            f"resource-path: [{json.dumps(str(source.parent))}]\n"
        )
        build = tmp / f"{source.stem}.ipynb"
        if source.suffix == ".py":
            build.write_text(json.dumps(marimo_to_ipynb(source, tmp)), encoding="utf-8")
        else:
            shutil.copyfile(source, build)
        cmd = ["quarto", "render", build.name, "--to", fmt, "-M", "embed-resources:true", *quarto_args]
        done = subprocess.run(cmd, cwd=tmp, capture_output=True, text=True)
        result = tmp / f"{source.stem}.html"
        if done.returncode != 0 or not result.exists():
            raise RenderError(f"quarto render failed:\n{done.stderr or done.stdout}")
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(result, output)


RELOAD_JS = """<script>
(function () {
  var key = "dsestu-render-scroll", version = "%s", saved = sessionStorage.getItem(key);
  sessionStorage.removeItem(key);
  if (saved !== null) {
    var y = +saved, stop = false, until = Date.now() + 3000;
    history.scrollRestoration = "manual";
    ["wheel", "keydown", "touchstart", "mousedown"].forEach(function (e) {
      addEventListener(e, function () { stop = true; }, { once: true, passive: true });
    });
    // plots and tables draw after load and grow the page, so keep re-applying the scroll until they settle
    new ResizeObserver(function () { if (!stop && Date.now() < until) scrollTo(0, y); }).observe(document.body);
    scrollTo(0, y);
  }
  setInterval(function () {
    fetch("/__version", { cache: "no-store" }).then(function (r) { return r.text(); }).then(function (v) {
      if (v !== version) { sessionStorage.setItem(key, scrollY); location.reload(); }
    }).catch(function () {});
  }, 500);
})();
</script>"""


def watch(source: Path, output: Path, fmt: str, quarto_args: list[str], port: int, open_browser: bool) -> None:
    state = {"version": 0}

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/__version":
                body, ctype = str(state["version"]).encode(), "text/plain"
            elif self.path == "/":
                page = output.read_text(encoding="utf-8") if output.exists() else "<p>Waiting for the first successful render...</p></body>"
                head, sep, tail = page.rpartition("</body>")
                page = head + RELOAD_JS % state["version"] + sep + tail if sep else page + RELOAD_JS % state["version"]
                body, ctype = page.encode("utf-8"), "text/html; charset=utf-8"
            else:
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

    try:
        server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    except OSError:
        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{server.server_address[1]}/"

    watched = [source, session_file(source)] if source.suffix == ".py" else [source]

    def stamp():
        return tuple(p.stat().st_mtime_ns if p.exists() else 0 for p in watched)

    def build():
        started = time.monotonic()
        try:
            render(source, output, fmt, quarto_args)
        except RenderError as e:
            print(f"error: {e}", file=sys.stderr)
            return
        state["version"] += 1
        print(f"rendered {output} in {time.monotonic() - started:.1f}s", flush=True)

    build()
    print(f"live preview at {url} (watching {', '.join(p.name for p in watched)}; Ctrl+C to stop)", flush=True)
    if open_browser:
        webbrowser.open(url)
    last = stamp()
    try:
        while True:
            time.sleep(0.5)
            now = stamp()
            if now != last:
                time.sleep(0.3)  # marimo writes the .py and the session file a moment apart
                last = stamp()
                build()
    except KeyboardInterrupt:
        server.shutdown()


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="dsestu-render",
        allow_abbrev=False,
        description="Render a marimo (.py) or Jupyter (.ipynb) notebook with a dsestu Quarto template, without executing it.",
        epilog="Other options go to `quarto render`, e.g. -M title:'My report' or --metadata-file meta.yml.",
    )
    parser.add_argument("source", type=Path, help="notebook.py (marimo) or notebook.ipynb")
    parser.add_argument("-o", "--output", type=Path, help="output HTML (default: next to the source)")
    parser.add_argument("--to", default="dsestu-dark-html", help="Quarto format (default: %(default)s)")
    parser.add_argument("-w", "--watch", action="store_true", help="re-render on change and live-reload the browser")
    parser.add_argument("--port", type=int, default=4848, help="live preview port (default: %(default)s)")
    parser.add_argument("--no-open", action="store_true", help="don't open the browser in --watch mode")
    args, quarto_args = parser.parse_known_args(argv)

    source = args.source.resolve()
    if source.suffix not in (".py", ".ipynb") or not source.is_file():
        parser.error(f"{args.source} is not a .py or .ipynb file")
    output = (args.output or source.with_suffix(".html")).resolve()

    if args.watch:
        watch(source, output, args.to, quarto_args, args.port, not args.no_open)
        return
    try:
        render(source, output, args.to, quarto_args)
    except RenderError as e:
        sys.exit(f"error: {e}")
    print(f"rendered {output}")
