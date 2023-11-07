#!/usr/bin/python3

"""This module is for write_file function"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    and returns the number of characters written.

    Args:
        filename: the file name
        text: text should written in file
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
