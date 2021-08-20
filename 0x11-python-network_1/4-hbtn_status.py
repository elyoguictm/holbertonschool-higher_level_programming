#!/usr/bin/python3
""" Python script that fetches """

import requests


if __name__ == "__main__":
    hburl = 'https://intranet.hbtn.io/status'
    req = requests.get(hburl)
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(req.text), req.text))
