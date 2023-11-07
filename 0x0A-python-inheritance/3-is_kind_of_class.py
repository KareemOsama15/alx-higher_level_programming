#!/usr/bin/python3

"""This module is foris_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Args:
        obj: an object
        a_class: the class

    Returns:
        True if instance of class or class inherited from or False if not
    """

    return (isinstance(obj, a_class))
