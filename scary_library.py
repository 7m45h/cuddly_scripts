#!/usr/bin/env python

from urllib.parse import urlparse
from html.parser import HTMLParser

input_file = "/home/tmash/workspace/dev/warehouse/bookmarks.html"

class mrParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == "href":
                print(f'<a href="{urlparse(attr[1]).scheme}://{urlparse(attr[1]).hostname}/" target="_blank">{urlparse(attr[1]).hostname} &#8599;</a>')

parser = mrParser()

with open(input_file, "r") as file:
    parser.feed(file.read())
