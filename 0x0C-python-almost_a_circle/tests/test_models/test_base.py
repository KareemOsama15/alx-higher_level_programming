#!/usr/bin/python3

"""This module is unittest for Base class"""
import unittest
from models.base import Base
# from models.rectangle import Rectangle
# from models.square import Square


class TestBaseClass(unittest.TestCase):
    """TestBaseClass is a class that test Base class"""

    def test_Base_id(self):
        """test nb_objects and id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_id_string(self):
        """test id by pass a string"""
        b1 = Base('15')
        self.assertEqual(b1.id, '15')

    def test_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """ Test accessing to private attributes """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects
