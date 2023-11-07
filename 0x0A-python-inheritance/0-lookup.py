#!/usr/bin/python3
"""This module is for lookup function"""


def lookup(obj):
    """
    function returns list of available attributes and methods of an object.

    Args:
        obj: an object
    """
    return (dir(obj))
