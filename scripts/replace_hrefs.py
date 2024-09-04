import os

from bs4 import BeautifulSoup as bs
from bs4 import ResultSet, Tag

non_digital_pages = 'html/worldsfairs/'
digital_pages = 'html/worldsfairs/result/id/'

valid_hrefs = ['index', 'about', 'rights', 'browse', 'essays', 'exhibits', 'documentation', 'umd:']

def replace_href(a: Tag):
    href = a.get('href')
    if href is None:
        print(f'href not found in {a}')
        return

    if '.html' not in href:
        print(f'.html was not found in {href}')
        return

    if not any(s in href for s in valid_hrefs):
        print(f'invalid match found for {href}')
        return

    href = href.replace('.html', '')
    a['href'] = href

for file in os.listdir(non_digital_pages):
    if not file.endswith('.html'):
        continue

    with open(non_digital_pages + file) as f:
        parsed_html = bs(f, 'html.parser')

    tags: ResultSet = parsed_html.findAll('a')

    for a in tags:
        replace_href(a)

    with open(non_digital_pages + file, 'wb') as f:
        f.write(parsed_html.prettify('utf-8'))

for file in os.listdir(digital_pages):
    if not file.endswith('.html'):
        continue

    with open(digital_pages + file) as f:
        parsed_html = bs(f, 'html.parser')

    tags: ResultSet = parsed_html.findAll('a')

    for a in tags:
        replace_href(a)

    with open(digital_pages + file, 'wb') as f:
        f.write(parsed_html.prettify('utf-8'))
