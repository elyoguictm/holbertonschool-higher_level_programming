#!/usr/bin/python3
"""add_attribute """


def add_attribute(self, attribute, value):
    """Add attribute"""
    if hasattr(self, '__dict__'):
        setattr(self, attribute, value)
    else:
        raise TypeError("can't add new attribute")
