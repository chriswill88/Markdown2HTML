#!/usr/bin/python3
"""markdown2html - render markdown to html"""
import sys
import os

def eprint(*args, **kwargs):
    """stderr print"""
    print(*args, file=sys.stderr, **kwargs)


if __name__ == "__main__":
    toks = sys.argv

    if len(toks) < 2:
        eprint("Usage: ./markdown2html.py README.md README.html")
        exit(1)

    for filename in toks[1:]:
        if not os.path.exists(filename):
            eprint("Missing {}".format(filename))
            exit(1)
    exit(0)
