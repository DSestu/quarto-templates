---
name: dsestu-dark
description: Ink-and-cream reading world for rendered notebooks and books, with one sodium-amber accent.
colors:
  ink-950: "#0a0c11"
  ink-900: "#0e1116"
  ink-800: "#14181f"
  ink-700: "#1a1f27"
  ink-600: "#232934"
  ink-500: "#2e3543"
  ink-400: "#5a6373"
  ink-300: "#8a93a4"
  ink-200: "#bdc4d1"
  cream: "#e8e4d8"
  cream-bright: "#f4f1e6"
  amber: "#f0b232"
  amber-bright: "#f6c969"
  amber-soft: "rgba(240, 178, 50, 0.16)"
  paper-bg: "#f5f2ea"
  paper-bg-deep: "#ece8dc"
  paper-surface: "#efebe0"
  paper-surface-2: "#e6e1d3"
  paper-text: "#1a1f27"
  paper-text-muted: "#4a525e"
  paper-text-faint: "#7a8290"
  paper-border: "#d4cebd"
  paper-border-soft: "#e2dcca"
  paper-border-strong: "#b8b1a0"
  paper-amber: "#8c5c0e"
  paper-amber-deep: "#74490a"
  note-blue: "#8db3f0"
  tip-green: "#9dd9b6"
  important-rose: "#ed8c8c"
  caution-violet: "#c5a8e8"
typography:
  display:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "clamp(2.25rem, 4.5vw, 3.25rem)"
    fontWeight: 600
    lineHeight: 1.02
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "clamp(2rem, 3.5vw, 2.625rem)"
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: "-0.035em"
  title:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "clamp(1.375rem, 2.2vw, 1.625rem)"
    fontWeight: 550
    lineHeight: 1.2
    letterSpacing: "-0.022em"
  subtitle:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 550
    lineHeight: 1.18
    letterSpacing: "-0.022em"
  lead:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "1.1875rem"
    fontWeight: 350
    lineHeight: 1.5
    letterSpacing: "-0.005em"
  body:
    fontFamily: "Geist, -apple-system, BlinkMacSystemFont, system-ui, sans-serif"
    fontSize: "1.03125rem"
    fontWeight: 400
    lineHeight: 1.6
    fontFeature: "\"ss01\", \"ss03\", \"cv11\", \"kern\""
  nav:
    fontFamily: "Geist, system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 450
    lineHeight: 1.4
    letterSpacing: "-0.005em"
  label:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: "0.6875rem"
    fontWeight: 500
    letterSpacing: "0.14em"
  code:
    fontFamily: "Geist Mono, ui-monospace, monospace"
    fontSize: "0.875em"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  hairline: "2px"
  sm: "0.375rem"
  button: "0.4rem"
  control: "0.45rem"
  md: "0.5rem"
  lg: "0.6rem"
  pill: "999px"
spacing:
  cell: "0.75em 1em"
  block: "1.75em"
  page-gutter: "1.75rem"
  column-gap: "3rem"
  title-gap: "4rem"
  measure: "37rem"
  measure-narrow: "33rem"
  book-legend: "17rem"
  part-gap: "1.1rem"
components:
  button-primary:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.ink-900}"
    rounded: "{rounded.button}"
    padding: "0.5em 1em"
  button-primary-hover:
    backgroundColor: "{colors.amber-bright}"
    textColor: "{colors.ink-900}"
  toolbar-button:
    backgroundColor: "{colors.ink-800}"
    textColor: "{colors.ink-300}"
    rounded: "{rounded.control}"
    size: "34px"
  toolbar-button-active:
    textColor: "{colors.amber}"
  search-field:
    backgroundColor: "{colors.ink-800}"
    textColor: "{colors.cream}"
    rounded: "{rounded.sm}"
  code-block:
    backgroundColor: "{colors.ink-800}"
    textColor: "{colors.cream}"
    typography: "{typography.code}"
    rounded: "{rounded.lg}"
    padding: "1.125rem 1.25rem"
  inline-code:
    backgroundColor: "{colors.ink-700}"
    textColor: "{colors.cream-bright}"
    padding: "0.1em 0.4em"
  table-header:
    backgroundColor: "{colors.ink-800}"
    textColor: "{colors.ink-300}"
    typography: "{typography.label}"
    padding: "0.875em 1em"
  table-cell:
    textColor: "{colors.cream}"
    padding: "{spacing.cell}"
  category-pill:
    textColor: "{colors.ink-300}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.2em 0.65em"
  code-fold-summary:
    backgroundColor: "{colors.ink-800}"
    textColor: "{colors.ink-300}"
    rounded: "{rounded.button}"
    padding: "0.25rem 0.6rem 0.25rem 0.5rem"
  toc-link:
    textColor: "{colors.ink-300}"
    typography: "{typography.nav}"
  toc-link-active:
    textColor: "{colors.amber}"
  book-part-label:
    textColor: "{colors.ink-300}"
    typography: "{typography.label}"
  book-chapter:
    textColor: "{colors.ink-300}"
    typography: "{typography.nav}"
  book-chapter-current:
    textColor: "{colors.amber}"
  running-head:
    textColor: "{colors.ink-300}"
    typography: "{typography.label}"
---

# Design System: dsestu-dark

## Overview

**Creative North Star: "The Lamp-Lit Ledger"**

A notebook rendered as a document someone took care over: deep ink grounds, cream text, one warm sodium-amber light, and quiet mono labels that read like the column heads of a ledger. The page is dark by default and offers a paper-like light theme with the same structure and a deeper amber. Everything is Geist; Geist Mono carries every label, number and line of code. Density is that of a reading document, not an app: generous vertical rhythm, a left legend that is always present, and a capped reading measure in books.

Structure is drawn with 1px hairlines and tonal steps of ink, not with shadows or heavy boxes. Content containers (code, outputs, callouts, tables) are gently rounded and outlined; navigation chrome is flat and unboxed. Motion is soft and constant in the background (slow drifting underlines, a roaming light segment on container outlines, a slow wash in callout headers) and short and eased for state changes. All of it collapses under `prefers-reduced-motion`.

The book surface sits inside the same world: one contents list in the left legend, parts as small mono group labels over their chapters, and amber marking only where the reader is and where they stopped.

**Key Characteristics:**
- Ink-on-ink tonal layering with 1px hairline rules; shadows only on floating layers.
- One warm accent (amber) for links, current position and primary action.
- Geist throughout, Geist Mono uppercase-tracked labels for metadata, counts, table heads and running heads.
- Left-side legend (page TOC, or one contents list in books); no right margin column.
- Two themes with identical token names (`--c-*`), switched on `data-theme`.

## Colors

A cold blue-black ink scale carries ground, surface and rules; cream carries text; a single warm amber is the only accent, with four muted callout hues kept for semantic boxes.

### Primary
- **Sodium Amber** (amber): links, the active TOC entry and its dot, the current chapter, the running-head number, the last-read flag, focus outlines, the primary button, sort indicators. On paper it deepens to **Paper Amber** (paper-amber) so it holds on a light ground.
- **Amber Bright** (amber-bright): hover state of amber links and the primary button. On paper the hover goes darker instead (paper-amber-deep).
- **Amber Wash** (amber-soft): `<mark>` backgrounds and the 3px focus halo on search fields.

### Tertiary (semantic only)
- **Note Blue**, **Tip Green**, **Important Rose**, **Caution Violet** (note-blue, tip-green, important-rose, caution-violet): callout headers, with 7–8% tinted fills and ~26–28% tinted borders of the same hue. Warning callouts reuse amber. The same hues tint the per-level heading underlines (h2 blue, h3 green, h4 violet, h5 rose) and the cell-output outline (blue).

### Neutral
- **Deep Ink** (ink-950): the deepest ground (`--c-bg-deep`).
- **Page Ink** (ink-900): page ground (`--c-bg`), also the ground of the book legend and its mobile drawer.
- **Surface Ink** (ink-800): code blocks, table heads, controls, search fields (`--c-surface`).
- **Raised Ink** (ink-700): inline code fill and the soft hairline (`--c-surface-2`, `--c-border-soft`).
- **Rule Ink** (ink-600): standard 1px borders (`--c-border`).
- **Strong Rule** (ink-500): emphasised rules and scrollbar thumbs (`--c-border-strong`).
- **Faint Ink** (ink-400): dots, list markers, language tags, rules and other non-text marks (`--c-text-faint`). At 3.1:1 it is too low for reading text; labels and sub-entries use Muted Ink.
- **Muted Ink** (ink-300): secondary text: nav links, metadata, labels, chapter numbers (`--c-text-muted`).
- **Cream** (cream): body text. **Cream Bright** (cream-bright): headings, strong text, hovered nav.
- **Paper** set (paper-*): the light theme's equivalents, role for role.

### Named Rules
**The Single Lamp Rule.** Amber is the only accent. In navigation chrome (book contents list, TOC, running head) it means "you are here" or "you stopped here" and nothing else; in prose it is the link colour. Never use it for decoration inside navigation.

**The Same Names Rule.** Every colour is consumed through `--c-*` custom properties defined for both themes. Components never hard-code a theme hex.

## Typography

**Display Font:** Geist (with -apple-system, system-ui, sans-serif)
**Body Font:** Geist, with stylistic sets ss01, ss03 and cv11
**Label/Mono Font:** Geist Mono (with ui-monospace, SF Mono, Menlo)

**Character:** One neutral grotesque used at many weights (350 to 600, with 450 and 550 in between) instead of a pairing; tight negative tracking on large sizes, wide positive tracking on small mono labels. Loaded from Google Fonts as a variable font.

### Hierarchy
- **Display** (600, clamp 2.25–3.25rem, 1.02): the document title only.
- **Headline** (600, clamp 2–2.625rem, 1.05): h1 inside the body.
- **Title** (550, clamp 1.375–1.625rem, 1.2): h2 sections; each heading level gets a 1px drifting underline in its level's hue, fading in opacity from 0.95 (h1) to 0.18 (h6).
- **Subtitle** (550, 1.25rem): h3.
- **Lead** (350, 1.1875rem, 1.5): opening paragraph and document subtitle, in cream-bright or muted.
- **Body** (400, 1.03125rem / 16.5px, 1.6): prose. In books running text (paragraphs, lists, quotes, callouts) is capped at 37rem (about 70–75 characters), 33rem below 1280px where body drops to 16px; code cells, outputs and tables keep the full column width.
- **Nav** (450, 0.875rem, 1.4): TOC and chapter links; nested entries 0.8125rem at 400.
- **Label** (Geist Mono 500, 0.6875rem, 0.12–0.14em, uppercase; the smallest size in the system, nothing is set below it): title metadata line, table heads, category pills, code-fold summaries, the book running head and "Continue reading" label, footer. The TOC title is the smallest at 0.625rem / 0.18em.
- **Code** (Geist Mono 400, 0.875em, 1.6): code blocks and inline code; ligatures off on inline code.

### Named Rules
**The Mono Means Data Rule.** Geist Mono uppercase labels name real things: metadata, counts, column heads, part group labels, the part and chapter the reader is in. They are never added as decorative tags above a heading.

**The Tabular Numbers Rule.** Chapter numbers, table numerics and the running-head number use tabular figures.

## Layout

A two-column grid: a left legend column (`minmax(220px, 22vw)`, driven by `--toc-col-width`, 16rem for reports) and a fluid body column, with a 3rem column gap and 1.75rem page gutters. There is no right margin column. Content blocks sit 1.5–1.75em apart; headings open with 2.75em above; the title block closes with 4rem below (2.5rem in books).

Books widen the legend to 17rem and fill it with one contents list: book name, search, then each part as a group of chapters, groups 1.1rem apart. The page's own TOC nests under the current chapter, and the current chapter scrolls into view in the list on load. A running head (part number, part, chapter) sits in the page's head row level with the floating toolbar, not over the title. Previous / next links close the chapter between hairlines.

Responsive behaviour:
- **Below 1280px:** the legend leaves the grid and reappears as a floating overlay (17.5rem; 18.5rem in books): on hover from a 22px left-edge peek zone, or pinned open by the toolbar toggle, T, or (in books) a labelled "Contents" button at the start of the running head; Escape or a click outside closes it. On touch screens book list rows grow to about 40px, and below 992px the drawer drops its search box because Quarto's header carries one; body text drops to 16px, h1 to 2rem, h2 to 1.375rem.
- **Below 992px:** the running head hides (Quarto's header carries the breadcrumb) and the book legend opens as a full-height drawer under Quarto's header, up to 21rem wide.
- **Below 768px:** Quarto hides the TOC; the toggle and its reserved padding go with it.

## Elevation & Depth

Flat by default. Depth comes from tonal steps of ink (ground, surface, raised) and 1px hairlines; containers on the page carry no shadow. Shadows appear only on layers that float above the page, and those pair a soft drop with a faint amber 1px ring.

### Shadow Vocabulary
- **Control lift** (`0 1px 0 rgba(0,0,0,0.2), 0 4px 12px -4px rgba(0,0,0,0.35)`): fixed toolbar buttons (TOC, code fold, export, theme).
- **Overlay** (`0 10px 30px -6px rgba(0,0,0,0.45), 0 0 0 1px` amber at 12%): the peeking legend below 1280px.
- **Menu** (`0 12px 32px -10px rgba(0,0,0,0.5), 0 0 0 1px` amber at 10%): the export dropdown.
- **Drawer** (`0 18px 40px -12px rgba(0,0,0,0.5)`): the mobile book drawer.
- **Modal** (`0 30px 80px -12px rgba(0,0,0,0.6), 0 0 0 1px` amber at 10%): the source-preview panel.
- **Focus halo** (`0 0 0 3px` amber-soft): focused search field.

### Named Rules
**The Float Earns A Shadow Rule.** A surface gets a shadow only if it floats over content (fixed, overlay, menu, modal). Anything in the document flow is separated by tone and hairline.

## Shapes

Gently rounded containers, crisp everywhere else. Content containers round at 0.5rem (tables, callouts) or 0.6rem (code blocks, overlays); controls at 0.375–0.45rem; category pills are full pills; TOC dots are circles (4px, 7px when active). Borders are always 1px. Navigation chrome has no corners to speak of: the book contents list and TOC are unboxed text on the page ground.

## Components

### Buttons
- **Shape:** softly rounded (0.4rem), 1px border, padding 0.5em 1em, Geist 500.
- **Primary:** amber fill with page-ink text; hover lifts to amber-bright.
- **Outline:** amber text and border on transparent; hover fills amber.
- **Toolbar buttons:** 34px squares, surface fill, soft hairline, muted icon, control-lift shadow, light backdrop blur. When the thing they control is on, the icon turns amber over an 8% amber tint with a 42% amber border.

### Code blocks and inline code
- **Blocks:** surface fill, 1px rule border, 0.6rem radius, 1.125rem × 1.25rem padding, Geist Mono at 0.875em. A tracked mono language tag sits top right in faint ink; copy button on hover. Syntax colours come from theme-aware `--c-syntax-*` tokens.
- **Inline:** raised-ink fill, soft hairline, 0.3em radius, cream-bright text; amber when inside a link.
- **Code-fold summary:** a small mono uppercase chip (surface, soft hairline, 0.4rem radius) with a custom caret; consecutive collapsed folds fuse into one with a count badge.

### Tables
- **Frame:** 1px rule border, 0.5rem radius, transparent body.
- **Head:** surface fill, Geist Mono label style in muted ink.
- **Rows:** 0.75em × 1em cells, soft hairline between rows, a 2.5% cream hover wash; numerics right-aligned in tabular figures.
- **Interactive marimo table:** a search field and paging buttons (surface, 1px rule, 0.375rem radius) above and below a scroll pane capped at 36rem with a sticky head; sortable headers show the column type in faint ink and the sort direction in amber; disabled controls drop to 40% opacity.

### Callouts
- **Style:** tinted fill and tinted 1px border in the callout's hue (no thick left bar), 0.5rem radius, header in the hue at Geist 600.

### Navigation (page TOC)
- **Style:** a dot rail: each entry hangs off a 4px dot in faint ink, labels in muted ink at the nav size; nested entries smaller, fainter and indented while the dots stay column-aligned.
- **Hover:** label and dot go cream-bright.
- **Active:** label amber at 550, dot grows to 7px amber.
- **Title:** "Contents" in the smallest tracked mono label.

### Book Contents List
- **Order:** book name (Geist 600, 0.95rem, cream-bright, links to the book home), search field, then one group per part.
- **Search field:** surface fill, 1px rule, 0.375rem radius, amber border and 3px amber halo on focus, a `kbd` hint (Ctrl K / ⌘K) that hides on focus and on touch.
- **Part label:** Geist Mono label style in muted ink, a link (amber on hover) when the part has its own page. Loose pages such as a preface sit in a group with no label. Groups are 1.1rem apart.
- **Chapters:** tabular mono number plus title in muted ink at the nav size; hover goes to cream.
- **Current chapter:** amber at 550, number included, with the page TOC nested beneath it; it scrolls into view in the list on load.

### Running Head and Last-Read Flag
- **Running head:** Geist Mono uppercase at 0.6875rem / 0.12em: part number in amber, part in muted ink, chapter in cream.
- **Last-read flag:** a 12px filled flag in amber beside the last-read chapter in the contents list, kept per book in localStorage. On the book home a "Continue reading" line (mono label plus the chapter title at 550) sits between the title block's rule and a soft hairline.

### Previous / Next
- **Style:** two links split across the column under a soft hairline, muted at 550, chapter numbers in mono, arrows in amber; hover turns the link amber.

## Do's and Don'ts

### Do:
- **Do** consume colour through `--c-*` properties so both themes stay in step.
- **Do** separate in-flow regions with 1px hairlines (`--c-border-soft` in book chrome, `--c-border` around content containers) and tonal steps of ink.
- **Do** reserve amber inside navigation for the current position and the last-read flag.
- **Do** set labels, counts and running heads in Geist Mono uppercase with 0.12–0.14em tracking, and numbers in tabular figures.
- **Do** cap book running text at 37rem (33rem below 1280px) and let code cells, outputs and tables use the full column.
- **Do** give every looping or entering animation a `prefers-reduced-motion` exit.

### Don't:
- **Don't** put shadows on anything in the document flow; shadows belong to toolbar buttons, overlays, menus, drawers and modals.
- **Don't** use amber in the book contents list or TOC for anything except "you are here" or "you stopped here".
- **Don't** box navigation chrome into cards; the contents list and TOC sit unboxed on the page ground.
- **Don't** use a thick coloured left bar on callouts; their border is 1px all round in the callout's hue.
- **Don't** introduce a second typeface, or an accent hue beyond amber outside callouts, heading underlines and syntax highlighting.

Keyboard: single-letter shortcuts C (code fold), D (theme), T (contents), F (fold section under the cursor); Tab is left to the browser, a "Skip to content" link is the first focus stop, and Ctrl/⌘ K focuses book search.

Observed in the build and not part of the system: the document title and h1–h3 draw a shimmer with gradient text (`background-clip: text`); `.impeccable/config.json` carries detector ignore-values for Geist and Geist Mono to keep the incumbent faces.
