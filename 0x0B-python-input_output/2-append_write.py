#!/usr/bin/python3

"""appenfile """

def append_write(filename="", text=""):
    """appends a string to a text file (UTF8)"""
    with open(filename, "a", encoding="UTF8") as f:
        return f.write(text)
