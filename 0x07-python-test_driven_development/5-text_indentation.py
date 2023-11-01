#!/usr/bin/python3
"""
This module is for that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines
    after each of these characters: ., ? and :.

    Args:
        text: the text arguement

    Returns:
        no return

    Raises:
        TypeError: if text isn't string

    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    cpText = text[:]

    for delim in ".?:":
        list_text = cpText.split(delim)
        cpText = ""
        for i in list_text:
            i = i.strip(" ")
            cpText = i + delim if cpText == "" else cpText + "\n\n" + i + delim

    print(cpText[:-3], end="")
