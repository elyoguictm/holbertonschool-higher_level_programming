#!/usr/bin/python3
""" Python script that takes in a URL """

import requests
from sys import argv

if __name__ == "__main__":
    email = {'email': argv[2]}
    request = requests.post(argv[1], data=email)
    print = (request.text)
