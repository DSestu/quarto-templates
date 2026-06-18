# quarto-templates

A small collection of [Quarto](https://quarto.org) format extensions for rendering notebooks and `.qmd` files into HTML that doesn't look templated.

## Available templates

Pick a template from the table below. The **Format string** column is the literal value you put under `format:` in your YAML — everything else in this README uses that string verbatim. The **Preview** column links to a single-file rendered HTML of the demo notebook.

| Template | Format string | Preview | What it looks like |
|----------|---------------|---------|--------------------|
| **dsestu-dark** | `dsestu-dark-html` | [`previews/dsestu-dark.html`](previews/dsestu-dark.html) · [source](examples/dsestu-dark/) | Sober dark-mode template — Geist + Geist Mono, single sodium-amber accent, left-side TOC (~25% width), main content fills the rest (~75%). |

> [!NOTE]
> **Naming convention.** Format string = `<template-name>-<base-format>`. Every template in this repo is prefixed with `dsestu-` to avoid collisions with extensions you install from elsewhere — so `dsestu-dark` extends Quarto's `html` base format, giving `dsestu-dark-html`. If a future template named `dsestu-paper` ships with a PDF base, its string would be `dsestu-paper-pdf`.

> [!TIP]
> GitHub renders raw `.html` blobs as plaintext. To view a preview rendered, paste its URL into <https://htmlpreview.github.io/>, or — easiest — clone the repo and open `previews/<name>.html` locally.

To preview a template before installing, clone this repo and either:

```bash
# Pre-rendered single-file HTML (fastest)
open previews/dsestu-dark.html

# Or re-render from source
quarto render examples/dsestu-dark/template.qmd
```

---

## Use it in another project

Each template ships as a Quarto **format extension**. Install once per project, then reference it by its format string (see table above) from any `.qmd` or `.ipynb`.

### 1. Install the extensions

From the root of the project where you want to use a template:

```bash
quarto add DSestu/quarto-templates
```

That's the shorthand `<github-user>/<repo-name>` form Quarto resolves against GitHub. Equivalent explicit forms:

```bash
quarto add github.com/DSestu/quarto-templates             # full URL
quarto add github.com/DSestu/quarto-templates@main        # pin to a branch
quarto add github.com/DSestu/quarto-templates@v1.0.0      # pin to a tag (see "Pin to a version")
```

If the repo is **private**, give Quarto an authenticated git URL:

```bash
quarto add git@github.com:DSestu/quarto-templates.git     # via SSH
# — or —
quarto add https://<token>@github.com/DSestu/quarto-templates.git
```

This pulls **all** templates from the repo and writes them under your project's `_extensions/` directory. You only pick which one to use at the YAML level — installation is repo-wide. Commit `_extensions/` if you want collaborators to render with the same styling.

If `quarto add` doesn't work (offline, restricted network, etc.), see [Local install fallback](#local-install-fallback) below.

### 2. Make your project a Quarto project

Quarto only walks up the directory tree looking for `_extensions/` **when a project file is present** at the root. Without one, rendering a notebook from a subdirectory fails with:

```
ERROR: Unable to read the extension 'dsestu-dark'.
```

…even though `quarto list extensions` (which scans the current directory) reports the extension as installed. The fix is a one-line `_quarto.yml` at the same level where you installed the extension:

```yaml
# _quarto.yml — sits at the project root, next to _extensions/
project:
  type: default
```

That single declaration is enough — Quarto now treats the whole tree as one project and finds the extension from any notebook beneath it.

You can also push the format default into the same file so notebooks don't need to repeat it in every raw cell:

```yaml
# _quarto.yml
project:
  type: default

format:
  dsestu-dark-html: default       # ← format string from the table
```

With this in place, any `.qmd` or `.ipynb` under the project root renders with the template automatically. Notebooks can still override or extend (title, author, categories, etc.) in their raw cell — they just don't need to re-declare the format.

> [!NOTE]
> Adding `_quarto.yml` makes the directory a Quarto project. The practical effect: `quarto render` with no arguments will try to build every renderable file under the root. To run a single file, name it explicitly: `quarto render path/to/notebook.ipynb`.

### 3. Select the template

Take the **Format string** from the [table above](#available-templates) and drop it under `format:`. The examples below use `dsestu-dark-html`; swap it for any other template's format string to switch.

#### In a Quarto markdown file (`.qmd`)

```yaml
---
title: My analysis
format:
  dsestu-dark-html: default       # ← format string from the table
---
```

Render with `quarto render notebook.qmd`.

#### In a Jupyter notebook (`.ipynb`)

You have two options.

**Option A — Project-wide via `_quarto.yml`.** Drop this next to your notebook(s):

```yaml
# _quarto.yml
format:
  dsestu-dark-html: default       # ← format string from the table
```

Every `.ipynb` in that directory inherits the format. Render with `quarto render notebook.ipynb`.

**Option B — Per-notebook via a raw cell.** In the first cell of the notebook, set the cell type to **Raw** (not Markdown, not Code) and paste:

```yaml
---
title: My analysis
author: Your Name
date: today
format:
  dsestu-dark-html: default       # ← format string from the table
---
```

Render with `quarto render notebook.ipynb`.

> [!TIP]
> In JupyterLab / VS Code, change the cell type via the dropdown above the cell (or `Esc` then `R` in JupyterLab). The raw cell must contain ONLY the YAML, fenced by `---` lines.

### 4. Render

```bash
quarto render notebook.ipynb       # single file
quarto render                       # everything in the project
quarto preview notebook.ipynb       # live-reload during writing
```

### Switching templates

To change which template a project uses, edit only the format string under `format:` (in the `.qmd` front-matter, `_quarto.yml`, or the notebook's raw cell). Installation is shared — `_extensions/` already contains every template from this repo, so no re-install is needed when switching.

The output HTML is fully self-contained except for the Google Fonts request to `fonts.googleapis.com` (Geist + Geist Mono). Add `embed-resources: true` under the format if you need a single offline-portable HTML file.

---

## Keeping templates up to date

Templates are **vendored** into each consumer project under `_extensions/`. That means edits to this repo do **not** automatically reach projects that have already installed it — you have to pull them in.

### Pull the latest version

From the root of any project that has the extension installed:

```bash
quarto update DSestu/quarto-templates
```

Quarto compares the installed version against the remote, downloads any changes, and overwrites the local `_extensions/dsestu-*` directories. It will prompt before overwriting if you've edited the files locally.

If `quarto update` doesn't recognise the source (rare), `quarto add DSestu/quarto-templates` does the same thing — it re-adds and overwrites.

### Check what's installed

```bash
quarto list extensions          # ← shows installed extensions + versions
```

### Pin to a version

Every release of this repo is tagged. To install a specific tag instead of `main`:

```bash
quarto add DSestu/quarto-templates@v1.0.0
quarto update DSestu/quarto-templates@v1.0.0
```

Useful when you want a notebook to keep rendering the same way even after the template evolves.

### Heads-up if you edit the extension locally

If you tweaked `_extensions/dsestu-dark/styles.css` inside a consumer project, `quarto update` will ask before overwriting — choose carefully. To preserve your changes without forking, move them into a project-local `custom.scss` as described in [Customise without forking](#customise-without-forking).

---

## Local install fallback

If you can't `quarto add` from a remote (private repo, no network), clone this repo somewhere and copy the extension you want into your project:

```bash
git clone https://github.com/DSestu/quarto-templates.git /tmp/quarto-templates
mkdir -p _extensions
cp -r /tmp/quarto-templates/_extensions/dsestu-dark _extensions/dsestu-dark
```

Then use the format as documented above. To update later, `git pull` in the clone and re-copy.

---

## Customise without forking

Every visual choice in the `dsestu-dark` template is driven by CSS custom properties on `:root` defined in [`_extensions/dsestu-dark/theme.scss`](_extensions/dsestu-dark/theme.scss). To change the accent in a single project without forking, add a tiny `custom.scss` in your project root:

```scss
/*-- scss:rules --*/
:root {
  --c-accent:        #6ab0f0;   /* instrument cyan, instead of amber */
  --c-accent-bright: #93c8ff;
}
```

…and reference it in your project YAML:

```yaml
format:
  dsestu-dark-html:
    theme: [cosmo, _extensions/dsestu-dark/theme.scss, custom.scss]
```

Same trick works for fonts: drop a `custom.scss` that overrides `--bs-font-sans-serif` and any heading rules. Because `custom.scss` lives in the consumer project (not in `_extensions/`), `quarto update` won't touch it.

---

## Contributor setup

If you're working on this repo (editing templates, adding new ones), activate the tracked git hooks once after cloning:

```bash
git config core.hooksPath hooks
```

That points git at [`hooks/`](hooks/) instead of `.git/hooks/`, so the pre-commit hook described below runs automatically.

### Pre-commit hook — auto-rebuilds previews

The hook at [`hooks/pre-commit`](hooks/pre-commit) re-renders any template whose source files (`_extensions/<name>/*` or `examples/<name>/*`) are part of the staged diff. The rendered single-file HTML is written to `previews/<name>.html` and `git add`-ed into the same commit.

- **Why pre-commit?** Previews are committed alongside source so the table in this README always points at the current state.
- **How it decides what to render.** Only templates whose sources are staged get re-rendered. Editing the README alone won't trigger a render.
- **What it produces.** A single self-contained HTML (CSS and JS inlined via `-M embed-resources:true`). Google Fonts links stay external — that's fine; the file is still portable.
- **Skipping the hook.** `git commit --no-verify` bypasses it. Use this sparingly — it leaves previews stale.
- **Running it manually.** Anytime, with or without staged changes:

  ```bash
  ./hooks/pre-commit
  ```

  Without staged changes, every template still re-renders if you `git add` its source first.

> [!IMPORTANT]
> Don't edit `previews/*.html` by hand — the hook overwrites them on the next render.

---

## Repository layout

```
quarto-templates/
├── _extensions/
│   └── dsestu-dark/                ← canonical extension (this is what `quarto add` pulls)
│       ├── _extension.yml          ← format declaration & defaults
│       ├── theme.scss              ← SCSS variables + CSS custom properties
│       └── styles.css              ← design rules
├── examples/
│   └── dsestu-dark/                ← live demo of the dsestu-dark template
│       ├── _quarto.yml
│       ├── template.qmd
│       └── _extensions/dsestu-dark ← symlink to ../../../_extensions/dsestu-dark
├── previews/
│   └── dsestu-dark.html            ← single-file render of the demo (auto-generated)
└── hooks/
    └── pre-commit                  ← regenerates previews/*.html before each commit
```

The symlink lets `examples/dsestu-dark/` render against the canonical extension files so edits don't need to be propagated.

---

## Adding a new template

1. Create `_extensions/dsestu-<name>/` with `_extension.yml`, `theme.scss`, `styles.css`.
2. Mirror it under `examples/dsestu-<name>/` with a `_quarto.yml` declaring `format: dsestu-<name>-html: default` and a `template.qmd` demoing every component.
3. Symlink `examples/dsestu-<name>/_extensions/dsestu-<name>` → `../../../_extensions/dsestu-<name>` so the example renders against the canonical files.
4. Add a row to the table at the top of this file. Set the **Preview** link to `previews/dsestu-<name>.html`.
5. Bump the version in `_extension.yml` (and tag a release) so consumer projects can `quarto update`.
6. Stage the new files and commit — the pre-commit hook will generate `previews/dsestu-<name>.html` automatically.

---

## Contributing changes back

Render the example, audit visually, then open a PR. To preview locally:

```bash
quarto preview examples/dsestu-dark/template.qmd
```

The preview server hot-reloads on SCSS / CSS / qmd edits.

---

## License

MIT — see `LICENSE`.
