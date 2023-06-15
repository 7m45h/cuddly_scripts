#!/usr/bin/env python

import argparse
import string
import random

_parser = argparse.ArgumentParser(description="generate random ascii strings to use as passwords")
_parser.add_argument("-s", default=10, required=False, type=int, help="password length", metavar="")
_parser.add_argument("-o", default=5, required=False, type=int, help="no of passwords to generate", metavar="")
_parser.add_argument("-L", action="store_true", required=False, help="ascii letters")
_parser.add_argument("-u", action="store_true", required=False, help="ascii uppercase")
_parser.add_argument("-l", action="store_true", required=False, help="ascii lowercase")
_parser.add_argument("-d", action="store_true", required=False, help="digits")
_parser.add_argument("-p", action="store_true", required=False, help="ascii punctuations")
_parser.add_argument("-w", action="store_true", required=False, help="space")
args = _parser.parse_args()

def printPass(length, ascii_list, output_size):
    for i in range(output_size):
        print(f"[{i}]","".join(random.choices(ascii_list, k=length)))

if (args.L or args.u or args.l or args.d or args.p):
    ascii_list = ""
    if (args.L):
        ascii_list += string.ascii_letters
    if (args.u):
        ascii_list += string.ascii_uppercase
    if (args.l):
        ascii_list += string.ascii_lowercase
    if (args.d):
        ascii_list += string.digits
    if (args.p):
        ascii_list += string.punctuation
    if (args.w):
        ascii_list += " "
    printPass(args.s, ascii_list, args.o + 1)
else:
    ascii_list = list(string.ascii_letters + string.digits + string.punctuation + " ")
    printPass(args.s, ascii_list, args.o + 1)

exit()
