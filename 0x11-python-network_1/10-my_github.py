#!/usr/bin/python3
""" Python script that takes your GitHub """

import requests
from sys import argv

if __name__ == '__main__':
    request = requests.get('https://api.github.com/user',
                           auth=(argv[1], argv[2]))
    try:
        print(r.json()['id'])
    except Exception:
        print('None')
