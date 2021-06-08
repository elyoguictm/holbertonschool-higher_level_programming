#!/usr/bin/python3
"""
This module defines the "Base" class
"""

import json
import os

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

    @classmethod
    def save_to_file(cls, list_objs):
        """This method writes the JSON string representation of <list_objs>
           to a file
        """
        filename = cls.__name__ + ".json"
        my_list = []
        if list_objs:
            for obj in list_objs:
                my_dict = cls.to_dictionary(obj)
                my_list.append(my_dict)
            json_str = cls.to_json_string(my_list)
        else:
            json_str = "[]"
        with open(filename, "w") as file:
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """This method returns an instance with all attributes already set"""
        if len(dictionary) == 1:
            dummy = cls(1)
            dummy.update(**dictionary)
        else:
            dummy = cls(2, 2)
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file."""
        filename = cls.__name__ + ".json"
        lists = []
        if os.path.exists(filename):
            with open(filename, "r") as file:
                for z in cls.from_json_string(file.read()):
                    lists.append(cls.create(**z))
        return lists
