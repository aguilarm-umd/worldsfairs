#!/usr/bin/env python

import json

from jinja2 import Environment, FileSystemLoader, select_autoescape

# Create the browse.html page.

# Load in the fair data
fairs = {}

with open('solr.json', 'r') as solr:
    data = json.load(solr)

    for doc in data['response']['docs']:
        pid = doc['pid']
        do_type = doc['doType']
        title = doc['displayTitle']
        fair = doc['wfFair_facet'][0]

        if fair not in fairs:
            fairs[fair] = []

        fairs[fair].append({
            "title": title,
            "pid": pid,
            "type": "Image" if do_type == "UMD_IMAGE" else "Essay",
        })

# Convert fairs to data for template processing

data = {"fairs": []}

fair_names = sorted(fairs.keys())

for fair_name in fair_names:
    fair = {
        "name": fair_name,
        "items": sorted(fairs[fair_name], key=lambda x: x["title"]),
    }
    data["fairs"].append(fair)

# Create browse.html from the Jinja template

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

template = env.get_template("browse.html.jinja")

print(template.render(data))
