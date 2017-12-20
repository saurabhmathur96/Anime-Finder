#!/usr/bin/env python3

# Convert anime.csv to json

import json, csv, operator

with open('anime.csv') as handle:
    table = [row for row in csv.DictReader(handle)]


table = list(sorted(table, key=operator.itemgetter('rating'), reverse=True))
with open('anime.json', 'w') as handle:
    json.dump(table, handle)    