#!/usr/bin/python3
"""MyInt """


class MyInt(int):
    """my int"""
    def __eq__(self, other):
        """checker eq"""
        return int(self) != int(other)

    def __ne__(self, other):
        """checker ne"""
        return int(self) == int(other)
