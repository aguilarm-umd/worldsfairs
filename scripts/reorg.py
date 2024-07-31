#!/usr/bin/env python

from pathlib import Path
import fileinput

# Reorganize the file layout as saved by wget

root = Path('.')
digital = root / 'digital.lib.umd.edu'
html = root / 'html'

if not digital.exists() or not digital.is_dir():
    raise Exception(f"{digital=} should exist and be a directory")

if html.exists():
    raise Exception(f"{html=} should not")

digital.rename(html)

# Rename worldsfairs.html to index.html
index = html / 'index.html'
(html / 'worldsfairs.html').rename(index)

# Move contents of html/worldsfairs to html
wf = html / 'worldsfairs'
for file in ('binaries', 'index.html', 'webfiles'):
    (html / file).rename(wf / file)
(html / 'robots.txt').unlink()

# Walk all html files
for dir, _, files in html.walk(on_error=print):
    for file in files:
        if file.endswith('.html'):

            # Update links in this file
            for line in fileinput.input(dir / file, inplace=True, backup='.bak', encoding="utf-8"):
                line = line.replace("../webfiles", "webfiles") \
                    .replace("../binaries", "binaries") \
                    .replace("../worldsfairs.html", "worldsfairs.html") \
                    .replace("worldsfairs.html", "index.html") \
                    .replace("worldsfairs/about.html", "about.html") \
                    .replace("worldsfairs/essays.html", "essays.html") \
                    .replace("worldsfairs/documentation.html", "documentation.html") \
                    .replace("worldsfairs/exhibits.html", "exhibits.html") \
                    .replace("worldsfairs/rights.html", "rights.html") \
                    .replace("worldsfairs/browse.html", "browse.html") \

                print(line, end='')
