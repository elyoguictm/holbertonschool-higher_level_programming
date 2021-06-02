#!/usr/bin/python3

"""Contains one function load_from_json_file()"""
import json


def load_from_json_file(filename):
    """creates an object"""
    with open(filename, "r", encoding="UTF8") as f:
        return json.loads(f.read())
