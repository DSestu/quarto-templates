# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

- **Authors:** David Sestu, a data scientist, and anyone who installs the templates. They write analyses in marimo notebooks, Jupyter notebooks, or `.qmd` files and need to turn them into something they can share.
- **Readers:** a mix of internal colleagues and external people such as clients and partners. They open a rendered HTML report someone sent them. Many are not technical, so the prose, charts and tables matter more to them than the code.

## Product Purpose

Turn notebooks and Quarto documents into HTML reports that don't look templated. Success means an author goes from a working notebook to a report fit for an outside reader in one command, and the reader can understand and explore the analysis without any tooling.

## Positioning

Two things a stock Quarto or Jupyter export doesn't do:
- `dsestu-render` renders marimo notebooks from the outputs the marimo editor already saved, so nothing is re-executed. Interactive plotly, vega and dataframe outputs stay interactive in the report.
- The templates themselves are designed, with their own identity instead of Quarto's default look.

## Operating Context

- Authors write in marimo (`.py`), Jupyter (`.ipynb`) or Quarto (`.qmd`). For marimo, they run the notebook once in the editor with autorun on startup turned off, so the outputs get saved.
- Two ways to render: `dsestu-render` (installable with `uvx` from the GitHub repo, with a `--watch` live preview), or `quarto render` with the extension installed through `quarto add`.
- The output is one self-contained `.html` file that people send around. It has to make sense with no server.
- Readers choose dark or light theme, collapse code, follow a left-side table of contents, and export the source (`.qmd`, `.ipynb`) from the page.

## Capabilities and Constraints

- Format extensions live under `_extensions/`. Format strings follow `<template>-<base-format>`, prefixed `dsestu-`. Only one template exists today: `dsestu-dark` (`dsestu-dark-html`).
- Rendering never executes notebooks. marimo tables keep only the first page of rows unless the author writes `mo.ui.table(df, pagination=False)`. Interactive marimo widgets such as sliders appear as static snapshots.
- Plotly, vega and Google Fonts currently load from CDNs, so a report needs network access to render fully.
- The pre-commit hook re-renders `previews/<template>.html` from `examples/<template>/`.
- **Planned, not yet decided:** a "book" style for multi-document websites, such as a personal knowledge base (`/home/david/github/knowledge`), built from these templates.
- **Open decisions:** whether single-file output, the no-execution rule, offline rendering, or the "doesn't look templated" goal take priority when they conflict.

## Brand Commitments

- Personal `dsestu` identity, not tied to any company brand.
- The README's stated goal is HTML "that doesn't look templated".

## Evidence on Hand

- Demo document: `examples/dsestu-dark/template.qmd`, pre-rendered to `previews/dsestu-dark.html`.
- Tests: `tests/test_dsestu_render.py`.
- No testimonials, users or usage numbers exist. Don't invent any.

## Product Principles

1. **The reader comes first.** Reports go to external and non-technical readers, so what the analysis says beats how it was coded.
2. **One command from notebook to report.** Every extra step an author has to take is a cost.
3. **Never re-run the author's work.** Render from saved outputs, and say clearly when something is missing instead of quietly degrading.
4. **Crafted, not templated.** Each template has its own point of view.
