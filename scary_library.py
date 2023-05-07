#!/usr/bin/env python

from html.parser import HTMLParser

input_file = "/home/tmash/workspace/dev/warehouse/bookmarks.html"
urls = ""

class mrParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0] == "href":
                print(attr[1])            

parser = mrParser()

with open(input_file, "r") as file:
    parser.feed(file.read())