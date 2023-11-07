#!/usr/bin/python3

"""This module for is_same_class function"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly an instance
    of the specified class ; otherwise False.

    Args:
        obj: an object
        a_class: the class

    Returns:
        true if instance of class otherwise false
    """

    return (type(obj) is a_class)
