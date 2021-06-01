#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """Check if object is an instance of a class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
