#!/usr/bin/env python3
"""Convert the DOMO Japan localization report (English) from Markdown to styled HTML."""

import markdown

INPUT = "report_v3_en.md"
OUTPUT = "DOMO_Japan_Market_Entry_Report_v3.html"

CSS = """
@page {
    size: A4;
    margin: 2cm 1.5cm;
}
@media print {
    body { font-size: 9pt; }
    h1 { page-break-before: always; }
    h1:first-of-type { page-break-before: avoid; }
    table { page-break-inside: avoid; }
    .no-print { display: none; }
}
* { box-sizing: border-box; }
body {
    font-family: "Helvetica Neue", "Arial", "Hiragino Kaku Gothic Pro", "Noto Sans JP", sans-serif;
    font-size: 11pt;
    line-height: 1.7;
    color: #1a1a2e;
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 30px;
    background: #fff;
}
h1 {
    font-size: 22pt;
    color: #1a365d;
    border-bottom: 3px solid #2b6cb0;
    padding-bottom: 10px;
    margin-top: 40px;
}
h2 {
    font-size: 15pt;
    color: #2b6cb0;
    border-bottom: 2px solid #bee3f8;
    padding-bottom: 5px;
    margin-top: 30px;
}
h3 {
    font-size: 13pt;
    color: #2c5282;
    margin-top: 20px;
}
h4 {
    font-size: 11pt;
    color: #2d3748;
    margin-top: 15px;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 12px 0;
    font-size: 10pt;
}
th {
    background: linear-gradient(135deg, #2b6cb0, #2c5282);
    color: white;
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
}
td {
    padding: 6px 10px;
    border-bottom: 1px solid #e2e8f0;
}
tr:nth-child(even) td {
    background-color: #f7fafc;
}
tr:hover td {
    background-color: #ebf8ff;
}
code, pre {
    font-family: "SF Mono", "Menlo", "Consolas", monospace;
    font-size: 9.5pt;
}
pre {
    background-color: #1a202c;
    color: #e2e8f0;
    padding: 15px;
    border-radius: 6px;
    overflow-x: auto;
    white-space: pre-wrap;
}
code {
    background-color: #edf2f7;
    padding: 2px 5px;
    border-radius: 3px;
    color: #c53030;
}
pre code {
    background: none;
    color: inherit;
    padding: 0;
}
blockquote {
    border-left: 4px solid #ed8936;
    background-color: #fffaf0;
    padding: 12px 18px;
    margin: 15px 0;
    font-size: 10pt;
    border-radius: 0 6px 6px 0;
}
strong {
    color: #1a365d;
}
hr {
    border: none;
    border-top: 2px solid #e2e8f0;
    margin: 35px 0;
}
ul, ol {
    margin: 8px 0;
    padding-left: 22px;
}
li {
    margin: 4px 0;
}
.print-btn {
    position: fixed;
    top: 20px;
    right: 20px;
    background: #2b6cb0;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 14px;
    cursor: pointer;
    font-weight: bold;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    z-index: 1000;
}
.print-btn:hover {
    background: #2c5282;
}
"""

with open(INPUT, "r", encoding="utf-8") as f:
    md_text = f.read()

html_body = markdown.markdown(
    md_text,
    extensions=["tables", "fenced_code", "toc"],
    output_format="html5",
)

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DOMO Japan Market Entry — Comprehensive Report v3</title>
<style>{CSS}</style>
</head>
<body>
<script src="auth.js"></script>
<button class="print-btn no-print" onclick="window.print()">Save as PDF (Cmd+P)</button>
{html_body}
</body>
</html>"""

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"HTML generated: {OUTPUT}")
print("Open in browser and use Cmd+P → Save as PDF")
