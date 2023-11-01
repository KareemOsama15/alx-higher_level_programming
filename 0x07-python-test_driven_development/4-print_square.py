#!/usr/bin/python3
"""This module is for function that prints a square with the character #"""


def print_square(size):
    """
    Function that prints a square with the character #.

    Args:
        size: firts name

    Returns:
        no return

    Raises:
        TypeError: if size isn't integer
        ValueError: if size less than 0

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
