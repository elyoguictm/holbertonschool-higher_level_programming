#!/usr/bin/python3
"""
This module defines the "Base" class
"""

import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init Base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json"""
        if list_dictionaries is None or list_dictionaries == []:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """return list json"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
