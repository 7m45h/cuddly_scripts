#!/usr/bin/env python

import sqlite3
import argparse

parser = argparse.ArgumentParser(description="manage evil databse")
parser.add_argument("mode", choices=["l", "a", "u", "g", "d", "n"], help="l: list all a: add new u: update g: get info d: delete n: new table")
args = parser.parse_args()

con = sqlite3.connect("../warehouse/evil.db")
cur = con.cursor()

def newDatabase():
    cur.execute("CREATE TABLE torrents(hash TEXT, name TEXT, isMovie INTEGER, year INTEGER, imdb TEXT)")
    con.commit()

def addNew():
    print("[?]")
    name = input("    name: ")
    year = input("    year: ")
    imdb = input("    imdb: ")
    hash = input("    hash: ")

if (args.mode == "n"):
    newDatabase()
elif (args.mode == "d"):
    print("delete")
elif (args.mode == "u"):
    print("update")
elif (args.mode == "a"):
    print("add")
elif (args.mode == "g"):
    print("get")
else:
    print("list")

con.close()
exit()