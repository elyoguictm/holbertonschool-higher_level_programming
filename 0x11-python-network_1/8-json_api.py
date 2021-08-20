#!/usr/bin/python3
""" Python script that takes in a letter """
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    values = {'q': q}
    request = requests.post('http://0.0.0.0:5000/search_user', data=values)
    try:
        dict = request.json()
        id = dict.get('id')
        name = dict.get('name')

        if len(dict) == 0 or id is None or name is None:
            print("No result")
        else:
            print("[{}] {}".format(dict.get('id'), dict.get('name')))
    except:
        print("Not a valid JSON")
