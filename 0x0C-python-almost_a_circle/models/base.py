#!/usr/bin/python3
"""This module for class Base"""
import json
import os.path


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """method that defines class Base objects"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """method that returns the JSON string representation"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """method that writes the JSON string representation to a file"""
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if list_objs is None:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    def from_json_string(json_string):
        """method that returns list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """method returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return (new)

    @classmethod
    def load_from_file(cls):
        """method that returns a list of instances"""

        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename) is False:
            return []
        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []
        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))
        return list_ins
