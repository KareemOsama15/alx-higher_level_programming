#!/usr/bin/python3
"""This module is for function that first_name and last_name."""


def say_my_name(first_name, last_name=""):
    """
    Function that first_name and last_name.

    Args:
        first_name: firts name
        last_name: last name

    Returns:
        no return

    Raises:
        TypeError: if (first_name or last_name) isn't string

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
