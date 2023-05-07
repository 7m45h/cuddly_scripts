#!/usr/bin/env python

import sqlite3
import argparse

parser = argparse.ArgumentParser(description="manage evil databse")
parser.add_argument("mode", choices=["l", "a", "u", "g", "d", "n"], help="l: list all a: add new u: update g: get info d: delete n: new table")
args = parser.parse_args()

def newDatabase(name):
    print(f"new database {name}")

if (args.mode == "n"):
    newDatabase("test")
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