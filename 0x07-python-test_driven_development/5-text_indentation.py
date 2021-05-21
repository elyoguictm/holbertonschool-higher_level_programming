#!/usr/bin/python3
"""text_indentation module"""


def text_indentation(text):
    """adds 2 new lines after characters: '.?:'
    Args:
        text: text (str): text
    Raises:
        TypeError: in case text's type is not a string
    Return: Nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [row.strip(" ") for row in text.split(delim)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
