#!/usr/bin/python3
def add_attribute(obj, name, value):
    """
    function that adds a new attribute to an object if it’s possible

    Args:
        obj: an object
        name: attribute name
        value: attribute value

    Raises:
        TypeError: if the object can’t have new attribute

    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
