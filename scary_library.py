#!/usr/bin/env python

import json

input_file = "/home/tmash/workspace/dev/harbor/bookmarks.json"

with open(input_file, "r") as file:
    data = json.loads(file.read())
    print(json.dumps(data["children"][0]["children"], indent=4))