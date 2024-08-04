#!/usr/bin/env python

import json
import csv

# Generate CSV inventory

with open('data/solr.json', 'r') as solr:
    data = json.load(solr)

    with open('data/inventory.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['pid','handle','type','title','fair','identifier'])

        for doc in data['response']['docs']:
            pid = doc['pid']
            handle = doc['handle'][0]
            type = doc['doType']
            title = doc['displayTitle']
            fair = doc['wfFair_facet'][0]
            identifier = doc['dmIdentifier'][0]

            writer.writerow([pid, handle, type, title, fair, identifier])
