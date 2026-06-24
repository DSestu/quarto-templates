-- source-export.lua
--
-- Embeds the original source file (.qmd or .ipynb) into the rendered HTML
-- as a hidden <textarea> so the client-side JS can offer download buttons
-- for both formats. If the source is .ipynb, outputs are stripped before
-- embedding. The opposite-format export is generated in the browser at
-- download time (simple cell-fence conversion).

local function read_file(path)
  local f = io.open(path, "r")
  if not f then return nil end
  local content = f:read("*a")
  f:close()
  return content
end

local function html_escape(s)
  return (s
    :gsub("&", "&amp;")
    :gsub("<", "&lt;")
    :gsub(">", "&gt;"))
end

local function strip_ipynb_outputs(content)
  local ok, nb = pcall(quarto.json.decode, content)
  if not ok or type(nb) ~= "table" or type(nb.cells) ~= "table" then
    return content
  end
  for _, cell in ipairs(nb.cells) do
    if cell.cell_type == "code" then
      cell.outputs = {}
      cell.execution_count = nil
    end
  end
  local ok2, encoded = pcall(quarto.json.encode, nb)
  if ok2 then return encoded end
  return content
end

local function basename(path)
  local b = path:match("([^/\\]+)$") or path
  return (b:gsub("%.qmd$", ""):gsub("%.ipynb$", ""))
end

function Meta(meta)
  local input = quarto.doc.input_file
  if not input or input == "" then return meta end

  local source = read_file(input)
  if not source then return meta end

  local is_ipynb = input:match("%.ipynb$") ~= nil
  local kind = is_ipynb and "ipynb" or "qmd"
  local payload = is_ipynb and strip_ipynb_outputs(source) or source
  local base = basename(input)

  local html = table.concat({
    '<textarea hidden id="dsestu-source" data-kind="' .. kind ..
      '" data-name="' .. base .. '">',
    html_escape(payload),
    '</textarea>'
  }, "")

  quarto.doc.include_text("after-body", html)
  return meta
end
