#!/usr/bin/env python

import os
import csv
import base64
import string
import hashlib
import argparse

parser = argparse.ArgumentParser(description="evil list manager")
parser.add_argument("mode", choices=["l", "w", "f"], help="l: list w: write f: get html output")
args = parser.parse_args()

evildb_path = "/home/tmash/documents/general/evildb.csv"

def listData():
    if (os.path.isfile(evildb_path)):
        with open(evildb_path, "r") as dbfile:
            reader = csv.DictReader(dbfile, delimiter="\t")
            row_c = 0
            for row in reader:
                print(f"[{row_c}]")
                print(f"    id: {row['id']}")
                print(f"    name: {row['name']}")
                print(f"    year: {row['year']}")
                print(f"    imdb: {row['imdb']}")
                print(f"    hash: {row['hash']}")
                print("")
                row_c += 1
    else:
        print("[!] no db file found")

def writeData():
    name = input("[?] name: ")
    year = input("[?] year: ")
    imdb = input("[?] imdb: ")
    hash = input("[?] hash: ")

    row_id = f"{name}{year}".translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.whitespace)).lower()
    id = base64.b85encode(hashlib.md5(row_id.encode("ascii")).digest()).decode("ascii")

    if (os.path.isfile(evildb_path)):
        with open(evildb_path, "r") as dbfile:
            reader = csv.DictReader(dbfile, delimiter="\t")
            for row in reader:
                if (id == row["id"]):
                    print("[!] match found")
                    print(f"    id: {row['id']}")
                    print(f"    name: {row['name']}")
                    print(f"    year: {row['year']}")
                    print(f"    imdb: {row['imdb']}")
                    print(f"    hash: {row['hash']}")

                    print("[?] quit or write anyway (q/w)")
                    quit = input(": ")

                    if (quit == "q"):
                        exit()
                    else:
                        break

    print("[!] summery")
    print(f"    id: {id}")
    print(f"    name: {name}")
    print(f"    year: {year}")
    print(f"    imdb: {imdb}")
    print(f"    hash: {hash}")

    print("[?] write to disk (y/n)")
    write = input(": ")

    if (write == "y"):
        update = { "id": id, "name": name, "year": year, "imdb": imdb, "hash": hash }
        if (os.path.isfile(evildb_path)):
            with open(evildb_path, "a") as dbfile:
                writer = csv.DictWriter(dbfile, fieldnames=update.keys(), delimiter="\t")
                writer.writerow(update)
        else:
            with open(evildb_path, "w") as dbfile:
                writer = csv.DictWriter(dbfile, fieldnames=update.keys(), delimiter="\t")
                writer.writeheader()
                writer.writerow(update)
    else:
        writeData()

def getHtml():
    if (os.path.isfile(evildb_path)):
        with open(evildb_path, "r") as dbfile:
            reader = csv.DictReader(dbfile, delimiter="\t")
            html = ""
            for row in reader:
                html += f'''
<div class="div-movie-main">
    <div class="div-movie-name">{row["name"]}</div>
    <a class="div-movie-imdb" href="https://www.imdb.com/title/{row["imdb"]}/" target="_blank" title="info on imdb">&#8599;</a>
</div>'''
        print(html)
    else:
        print("[!] no db file found")

if (args.mode == "w"):
    writeData()
elif (args.mode == "l"):
    listData()
else:
    getHtml()

exit()
