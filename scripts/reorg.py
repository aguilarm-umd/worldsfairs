#!/usr/bin/env python

from pathlib import Path
import fileinput

# Reorganize the file layout as saved by wget

root = Path('.')
digital = root / 'digital.lib.umd.edu'
html = root / 'html'
index = html / 'index.html'
wf = html / 'worldsfairs'

if not digital.exists() or not digital.is_dir():
    raise Exception(f"{digital=} should exist and be a directory")

if html.exists():
    raise Exception(f"{html=} should not")

digital.rename(html)

# Rename worldsfairs.html to index.html
(html / 'worldsfairs.html').rename(index)

# Move contents of html/worldsfairs to html
for file in ('binaries', 'index.html', 'webfiles'):
    (html / file).rename(wf / file)
(html / 'robots.txt').unlink()

# Walk all html files

for dir, _, files in html.walk(on_error=print):
    for file in files:
        if file.endswith('.html'):

            html_file = dir / file

            print(f"Updating {html_file}")

            txt = html_file.read_text(encoding="utf-8")

            # Update links in this file
            txt = txt \
                .replace("../webfiles", "webfiles") \
                .replace("../binaries", "binaries") \
                .replace("../worldsfairs.html", "worldsfairs.html") \
                .replace("worldsfairs.html", "index.html") \
                .replace("worldsfairs/about.html", "about.html") \
                .replace("worldsfairs/essays.html", "essays.html") \
                .replace("worldsfairs/documentation.html", "documentation.html") \
                .replace("worldsfairs/exhibits.html", "exhibits.html") \
                .replace("worldsfairs/rights.html", "rights.html") \
                .replace("worldsfairs/browse.html", "browse.html")

            # Update the "Search the Database" navbar link

            if file.startswith("umd:"):
                dummy_link=f"./{file}#"
                browse_link="../../browse.html"
            else:
                dummy_link=f"{file}#"
                browse_link="browse.html"

            browse_nav = (
                f'<li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="{dummy_link}">Search the Database</a>\n'
                ' <ul class="dropdown-menu">\n'
                "  <li><a href='https://digital.lib.umd.edu/worldsfairs/results'>Search</a></li>\n"
                f"  <li><a href='{browse_link}'>Browse</a></li>\n"
                ' </ul>\n'
                ' </li>\n'
            )

            if file.startswith("umd:"):
                browse_path = "../../browse.html"
            else:
                browse_path = "browse.html"

            txt = txt.replace(
                browse_nav,
                f"<li><a href=\"{browse_path}\">Browse the Database</a></li>\n"
            )

            # Write the file
            with open(html_file, "wt") as f:
                f.write(txt)
