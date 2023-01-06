from markdown import markdown as markdown_converter
from markdown.extensions.toc import TocExtension

html_filename = "../rules.html"
md_filename = "../rules.md"
header_filename = "html_header.html"

with open(md_filename, 'rt', encoding='utf-8') as md_file:
    with open(header_filename, 'rt', encoding='utf-8') as header_file:
        with open(html_filename, 'wt', encoding='utf-8') as html_file:
            html_file.write(header_file.read() + markdown_converter(md_file.read(), extensions=['extra', TocExtension(baselevel=1)]))