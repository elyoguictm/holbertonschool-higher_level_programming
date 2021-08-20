#!/usr/bin/python3
"""script that takes in a URL and an email"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    from sys import argv
    imp = argv[1]
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    request = urllib.request.Request(imp, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
