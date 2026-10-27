from dsestu_render import pick_data, pop_front_matter, to_ipynb_outputs

PNG = "data:image/png;base64,AAAA"


def _md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text}


def test_front_matter_cell_is_popped_plain_or_fenced():
    for text in ("---\ntitle: Report\ntags: [a, b]\n---", "\n```yaml\n---\ntitle: Report\ntags: [a, b]\n---\n```\n"):
        nb = {"cells": [{"cell_type": "code", "source": "x = 1"}, _md(text), _md("# Intro")]}
        assert pop_front_matter(nb) == "---\ntitle: Report\ntags: [a, b]\n---\n"
        assert [c["source"] for c in nb["cells"]] == ["x = 1", "# Intro"]


def test_front_matter_ignores_regular_markdown():
    nb = {"cells": [_md("Some text\n\n---\n\nmore text"), _md("```yaml\nkey: v\n```")]}
    assert pop_front_matter(nb) is None
    assert len(nb["cells"]) == 2


def test_pick_keeps_drawable_html_and_snapshots_widgets():
    plot = "<marimo-plotly data-figure='{}'></marimo-plotly>"
    assert pick_data({"text/html": plot, "image/png": PNG}) == {"text/html": plot}
    slider = "<marimo-ui-element><marimo-slider></marimo-slider></marimo-ui-element>"
    assert pick_data({"text/html": slider, "image/png": PNG}) == {"image/png": "AAAA"}
    lazy = "<marimo-table data-data='&quot;./@file/1.json&quot;'></marimo-table>"
    assert pick_data({"text/html": lazy, "image/png": PNG}) == {"image/png": "AAAA"}


def test_pick_warns_when_table_saved_only_first_page(capsys):
    rows = "&quot;[{&#92;&quot;a&#92;&quot;:1},{&#92;&quot;a&#92;&quot;:2}]&quot;"
    for total, warned in (("500", True), ("2", False)):
        table = f"<marimo-table data-data='{rows}' data-total-rows='{total}'></marimo-table>"
        assert pick_data({"text/html": table, "image/png": PNG}) == {"text/html": table}
        assert ("2 of its 500 rows" in capsys.readouterr().err) is warned


def test_pick_turns_vegalite_into_element():
    out = pick_data({"application/vnd.vegalite.v6+json": '{"mark": "point"}', "image/png": PNG})
    assert out == {"text/html": "<dsestu-vega data-spec='{&quot;mark&quot;: &quot;point&quot;}'></dsestu-vega>"}


def test_outputs_unwrap_bundle_then_console():
    cell = {
        "outputs": [{"type": "data", "data": {"application/vnd.marimo+mimebundle": '{"image/png": "%s", "__metadata__": {}}' % PNG}}],
        "console": [{"type": "stream", "name": "stdout", "text": "hi\n", "mimetype": "text/plain"}],
    }
    assert to_ipynb_outputs(cell) == [
        {"output_type": "display_data", "data": {"image/png": "AAAA"}, "metadata": {}},
        {"output_type": "stream", "name": "stdout", "text": "hi\n"},
    ]


NOTEBOOK = '''import marimo

app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
'''


def test_generic_cell_is_added_and_read_back_by_marimo(tmp_path):
    import json, subprocess, sys
    from dsestu_render import add_marimo_front_matter, generic_front_matter

    nb_path = tmp_path / "private_networks_france.py"
    nb_path.write_text(NOTEBOOK)
    meta = generic_front_matter(nb_path)
    assert 'title: "Private networks france"' in meta
    add_marimo_front_matter(nb_path, meta)
    out = tmp_path / "out.ipynb"
    subprocess.run([sys.executable, "-m", "marimo", "export", "ipynb", str(nb_path), "--sort", "top-down", "-o", str(out)], check=True, capture_output=True)
    nb = json.loads(out.read_text())
    assert pop_front_matter(nb) == meta


def test_ipynb_gets_raw_cell_once(tmp_path):
    import json
    from dsestu_render import ensure_ipynb_front_matter

    path = tmp_path / "report.ipynb"
    path.write_text(json.dumps({"nbformat": 4, "nbformat_minor": 5, "metadata": {}, "cells": [{"id": "a", "cell_type": "markdown", "metadata": {}, "source": "hi"}]}))
    ensure_ipynb_front_matter(path)
    ensure_ipynb_front_matter(path)
    cells = json.loads(path.read_text())["cells"]
    assert [c["cell_type"] for c in cells] == ["raw", "markdown"]
    assert cells[0]["id"] == "front-matter" and "".join(cells[0]["source"]).startswith('---\ntitle: "Report"')
