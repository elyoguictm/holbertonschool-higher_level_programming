#!/usr/bin/python3
""" Python script that takes in a URL """

import requests
from sys import argv


if __name__ == "__main__":
    email = {'email': argv[2]}
    val = argv[1]
    request = requests.post(val, data=email)
    print = (request.text)
