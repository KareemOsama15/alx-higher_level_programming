#!/usr/bin/python3

"""This module is for read_file function"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: the file name
    """

    with open(filename, "r", encoding="utf-8") as f:
        read_text = f.read()
        print(read_text, end="")
