#!/usr/bin/env python

import string
import sqlite3
import argparse

parser = argparse.ArgumentParser(description="manage evil databse")
parser.add_argument("mode", choices=["l", "a", "d", "n"], help="l: list all a: add new d: delete n: new table")
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

if (args.mode == "n"):
    newDatabase()
elif (args.mode == "d"):
    deleteRow()
elif (args.mode == "a"):
    addNew()
else:
    listAll()

con.close()
exit()