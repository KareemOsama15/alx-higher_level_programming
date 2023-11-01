#!/usr/bin/python3
"""This Module is for function adds two numbers"""


def add_integer(a, b=98):
    """
    Function that add two numbers.

    Args:
        a: firts Number
        b: second number

    Returns:
        add the two numbers

    Raises:
        TypeError: 'a, b' must be an integers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
