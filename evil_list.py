#!/usr/bin/env python

import sqlite3
import argparse

parser = argparse.ArgumentParser(description="manage evil databse")
parser.add_argument("mode", choices=["l", "a", "u", "g", "d", "n"], help="l: list all a: add new u: update g: get info d: delete n: new table")
args = parser.parse_args()

con = sqlite3.connect("../warehouse/evil.db")
cur = con.cursor()

def newDatabase():
    cur.execute("CREATE TABLE IF NOT EXISTS torrents(hash TEXT, name TEXT, isMovie INTEGER, year INTEGER, imdb TEXT)")
    con.commit()
    print("[!] done")

def addNew():
    print("[?]")
    hash = input("    hash: ")
    if cur.execute("SELECT hash FROM torrents WHERE hash=?", (hash,)).fetchone() is None:
        name = input("    name: ")
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
            

if (args.mode == "n"):
    newDatabase()
elif (args.mode == "d"):
    print("delete")
elif (args.mode == "u"):
    print("update")
elif (args.mode == "a"):
    addNew()
elif (args.mode == "g"):
    print("get")
else:
    print("list")

con.close()
exit()