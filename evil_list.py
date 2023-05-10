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
    cur.execute("CREATE TABLE IF NOT EXISTS torrents(hash TEXT, name TEXT, isMovie INTEGER, year INTEGER, imdb TEXT)")
    con.commit()
    print("[!] done")

def addNew():
    print("[?]")
    hash = input("    hash: ").upper()
    if cur.execute("SELECT hash FROM torrents WHERE hash=?", (hash,)).fetchone() is None:
        name = input("    name: ").translate(str.maketrans(string.punctuation + string.whitespace, "_"*(len(string.punctuation) + len(string.whitespace)))).lower()
        movi = input("    movi: ")
        if movi == 1 or movi == "1":
            year = input("    year: ")
            imdb = input("    imdb: ")
            print("[!] summary")
            print(f"    hash: {hash}")
            print(f"    name: {name}")
            print(f"    year: {year}")
            print(f"    imdb: {imdb}")
            write = input("[?] write (y/n): ")
            if write == "y":
                cur.execute("INSERT INTO torrents VALUES (?, ?, ?, ?, ?)", (hash, name, movi, year, imdb))
                con.commit()
        elif movi == 0 or movi == "0":
            print("[!] summary")
            print(f"    hash: {hash}")
            print(f"    name: {name}")
            write = input("[?] write (y/n): ")
            if write == "y":
                cur.execute("INSERT INTO torrents VALUES (?, ?, ?, ?, ?)", (hash, name, movi, "", ""))
                con.commit()
        else:
            print("\n[!] invalid input")
    else:
        print("\n[!] torrent allready exists")

def listAll():
    for row in cur.execute("SELECT rowid, * FROM torrents").fetchall():
        print(f"[{row[0]}]\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}")

def deleteRow():
    id = input("[?] id: ")
    row = cur.execute("SELECT rowid, * FROM torrents WHERE rowid=?", (id,)).fetchone()
    print("[!]")
    print(f"[{row[0]}]\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}")
    delete = input("[?] delete (y/n): ")
    if delete == "y":
        cur.execute("DELETE FROM torrents WHERE rowid=?", (id,))
        con.commit()

def htmlOutput():
    for row in cur.execute("SELECT * FROM torrents WHERE isMovie=0").fetchall():
        print(f"""
<div class="div-movie-main">
    <div class="div-movie-name">{row[1]}</div>
    <a class="div-movie-imdb" href="https://www.imdb.com/title/{row[4]}">&#8599;</a>
</div>
""")

if args.mode == "n":
    newDatabase()
elif args.mode == "d":
    deleteRow()
elif args.mode == "a":
    addNew()
elif args.mode == "o":
    print("html output")
else:
    listAll()

con.close()
exit()