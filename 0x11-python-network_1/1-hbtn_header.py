#!/usr/bin/python3
""" Script that takes a URL, sends a request and returns"""

import urllib.request
import sys

if __name__ == "__main__":
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        print(response.info().get('X-Request-Id'))
