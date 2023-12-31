#!/usr/bin/python3

"""This module is for inherits_from function"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False.

    Args:
        obj: an object
        a_class: the class

    Returns:
        True if instance of class or class inherited from or False if not
    """
    if type(obj) is a_class:
        return (False)
    return (isinstance(obj, a_class))
