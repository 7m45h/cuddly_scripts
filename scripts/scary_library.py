#! /usr/bin/env python

import json

_input = "../warehouse/bookmarks.json"

with open(_input, 'r') as file:
    data = json.loads(file.read())

for folder in data['children'][1]['children'][0]['children']:
    print(folder['title'])
    for item in folder['children']:
        print(item['uri'])

exit()
