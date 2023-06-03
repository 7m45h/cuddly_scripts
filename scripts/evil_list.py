#!/usr/bin/env python

import string
import sqlite3
import argparse

parser = argparse.ArgumentParser(description="manage evil databse")
parser.add_argument("mode", choices=["n", "a", "l", "d", "o"], help="n: new table a: add l: list all d: delete o: html output")
args = parser.parse_args()

con = sqlite3.connect("../warehouse/evil.db")
cur = con.cursor()

def newDatabase():
    cur.execute("CREATE TABLE IF NOT EXISTS movies(imdb TEXT PRIMARY KEY ASC, name TEXT, year INTEGER, hash TEXT NULL, poster BLOB NULL)")
    con.commit()
    print("[!] done")

def addNew():
    print("[?]")
    imdb = input("    imdb: ")
    existing_row = cur.execute("SELECT imdb, name, year FROM movies WHERE imdb=?", (imdb,)).fetchone()
    if existing_row is None:
        name = input("    name: ")
        year = input("    year: ")
        hash = input("    hash: ").upper()
        poster = input("    poster: ")
        print("[!] summary")
        print(f"    hash: {imdb}")
        print(f"    name: {name}")
        print(f"    year: {year}")
        print(f"    imdb: {hash}")
        print(f"    imge: {poster}")

        with open(poster, "rb") as image:
            poster_bytes = image.read();

        write = input("[?] write to db (y/n): ")
        if write == "y":
            cur.execute("INSERT INTO movies VALUES (?, ?, ?, ?, ?)", (imdb, name, year, hash, poster_bytes))
            con.commit()
        else:
            print("\n[!] did not wrote to db")
    else:
        print("\n[!] allready exists")
        print(f"\n    imdb: {existing_row[0]}")
        print(f"\n    name: {existing_row[1]}")
        print(f"\n    year: {existing_row[2]}")

def listAll():
    for row in cur.execute("SELECT rowid, imdb, name, year, hash FROM movies").fetchall():
        print(f"[{row[0]}]\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")

def deleteRow():
    imdb = input("[?] imdb: ")
    row = cur.execute("SELECT rowid, name, year FROM movies WHERE imdb=?", (imdb,)).fetchone()
    print("[!]")
    print(f"[{row[0]}]\t{row[1]}\t{row[2]}")
    delete = input("[?] delete (y/n): ")

    if delete == "y":
        cur.execute("DELETE FROM movies WHERE imdb=?", (imdb,))
        con.commit()
        print("[!] done")
    else:
        print("[!] did not deleted")

def htmlOutput():
    for row in cur.execute("SELECT imdb, name, year, hash, poster FROM movies").fetchall():
        imdb = row[0]
        name = row[1]
        year = row[2]
        hash = row[3]
        poster_bytes = row[4]

        if poster_bytes is None:
            poster_path = "/evil_list/assets/posters/placeholder"
        else:
            poster_path = f"/evil_list/assets/posters/{imdb}"
            with open(f"../outputs/{imdb}", "wb") as image:
                image.write(poster_bytes)

        print(f"""
<div class="div-movie-card">
    <a href="https://www.imdb.com/title/{imdb}/" class="a-movie-poster">
        <img src="{poster_path}">
    </a>
    <a href="https://www.imdb.com/title/{imdb}/" class="a-movie-title">{name} {year}</a>
</div>
""")

if args.mode == "n":
    newDatabase()
elif args.mode == "d":
    deleteRow()
elif args.mode == "a":
    addNew()
elif args.mode == "o":
    htmlOutput()
else:
    listAll()

con.close()
exit()