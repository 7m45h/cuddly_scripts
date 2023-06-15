#! /usr/bin/env python

from urllib.parse import urlparse
from html.parser import HTMLParser

_inputFile = "/home/tmash/workspace/dev/warehouse/bookmarks.html"

class mrParser(HTMLParser):
    def handleStartTag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == "href":
                print(f'<a href="{urlparse(attr[1]).scheme}://{urlparse(attr[1]).hostname}/" target="_blank">{urlparse(attr[1]).hostname} &#8599;</a>')

_parser = mrParser()

with open(_inputFile, "r") as file:
    _parser.feed(file.read())
