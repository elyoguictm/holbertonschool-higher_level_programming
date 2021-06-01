#!/usr/bin/python3
"""print_sorted"""


class MyList(list):
    """class MyList"""

    def print_sorted(self):
        """Print list in ascending sort order"""
        print(sorted(self))
