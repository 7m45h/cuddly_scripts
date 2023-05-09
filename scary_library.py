#!/usr/bin/env python

from urllib.parse import urlparse
from html.parser import HTMLParser

input_file = "/home/tmash/workspace/dev/warehouse/bookmarks.html"

class mrParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == "href":
                print(f"""
<div class="div-link-main">
    <img class="div-link-fav" src="https://www.google.com/s2/favicons?domain={urlparse(attr[1]).hostname}&sz=128" loading="lazy"/>
    <a class="div-link-name" href="{attr[1]}">{attr[1]} &#8599;</a>
</div>                
""")

parser = mrParser()

with open(input_file, "r") as file:
    parser.feed(file.read())