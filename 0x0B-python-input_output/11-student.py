#!/usr/bin/python3
"""Class Student"""


class Student:
    """Studen def"""
    def __init__(self, first_name, last_name, age):
        """init student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict"""
        if attrs is None:
            return self.__dict__
        new = {}
        for at in attrs:
            try:
                new[at] = self.__dict__[at]
            except:
                pass
        return new

    def reload_from_json(self, json):
        """student inst"""
        for z in json:
            try:
                setattr(self, z, json[z])
            except:
                pass
