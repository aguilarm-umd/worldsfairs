#!/usr/bin/env python

from pathlib import Path
import re
import urllib.request
import json

# Fix images embedded in Essays which are too large

root = Path('.')
id = root / 'html' / 'worldsfairs' / 'result' / 'id'

# Walk all html files

for dir, _, files in id.walk(on_error=print):
    for file in files:
        if file.endswith('.html'):

            html_file = dir / file

            txt = html_file.read_text(encoding="utf-8")

            # Record updates to be made
            updates = []

            # Search for all matches
            for m in re.finditer(
                r'(https://iiif.lib.umd.edu/images/fedora2:umd:\d+)/full/!800,800/0/default.jpg',
                txt,
            ):
                full_url = m[0]
                base_url = m[1]
                info_url = base_url + '/info.json'

                # Get image info to determine if we need to fix the image size
                with urllib.request.urlopen(info_url) as url:
                    data = json.load(url)

                    size = max(data['width'], data['height'])
                    if size < 800:
                        fixed_url = base_url + f"/full/!{size},{size}/0/default.jpg"
                        updates.append((full_url, fixed_url))

            # Make the updates, if necessary
            if len(updates) > 0:
                print(f"Updating {html_file} with {len(updates)} URL updates")
                for full_url, fixed_url in updates:
                    txt = txt.replace(full_url, fixed_url)

                # Write the file
                with open(html_file, "wt") as f:
                    f.write(txt)
