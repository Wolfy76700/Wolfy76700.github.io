from markdown import markdown as markdown_converter
from markdown.extensions.toc import TocExtension

html_filename = ["../rules_den.html", "../rules_warrior.html", "../rules_pack.html"]
md_filename = ["../rules_den.md", "../rules_warrior.md", "../rules_pack.md"]
header_filename = ["html_header_den.html", "html_header_warrior.html", "html_header_pack.html"]

for i in range(len(html_filename)):
    with open(md_filename[i], 'rt', encoding='utf-8') as md_file:
        with open(header_filename[i], 'rt', encoding='utf-8') as header_file:
            with open(html_filename[i], 'wt', encoding='utf-8') as html_file:
                html_file.write(header_file.read() + markdown_converter(md_file.read(), extensions=['extra', TocExtension(baselevel=1)]))