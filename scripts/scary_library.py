#! /usr/bin/env python

import json
from urllib.parse import urlparse

_input = "../warehouse/bookmarks.json"
_output = """<ul id="list-web">"""

with open(_input, 'r') as file:
    data = json.loads(file.read())

for folder in data['children'][1]['children'][0]['children']:
    _output += f"<li>{folder['title']}</li><ul>"
    for item in folder['children']:
        _output += f"""<li><a class="anc-ext" href="{urlparse(item['uri']).scheme}://{urlparse(item['uri']).hostname}/" target="_blank">{urlparse(item['uri']).hostname} &#8599;</a></li>"""

    _output += "</ul>"

_output +="</ul>"

print(_output)

exit()
