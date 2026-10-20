from dsestu_render import front_matter, pick_data, to_ipynb_outputs

PNG = "data:image/png;base64,AAAA"


def test_front_matter_reads_comment_block_above_import():
    src = "# ---\n# title: Report\n# tags: [a, b]\n#\n# ---\nimport marimo\n# ---\n# title: no\n# ---\n"
    assert front_matter(src) == "title: Report\ntags: [a, b]\n"


def test_front_matter_absent():
    assert front_matter("import marimo\napp = marimo.App()\n") is None


def test_pick_keeps_drawable_html_and_snapshots_widgets():
    plot = "<marimo-plotly data-figure='{}'></marimo-plotly>"
    assert pick_data({"text/html": plot, "image/png": PNG}) == {"text/html": plot}
    slider = "<marimo-ui-element><marimo-slider></marimo-slider></marimo-ui-element>"
    assert pick_data({"text/html": slider, "image/png": PNG}) == {"image/png": "AAAA"}
    lazy = "<marimo-table data-data='&quot;./@file/1.json&quot;'></marimo-table>"
    assert pick_data({"text/html": lazy, "image/png": PNG}) == {"image/png": "AAAA"}


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
