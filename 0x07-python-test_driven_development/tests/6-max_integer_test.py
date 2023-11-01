#!/usr/bin/python3
"""This module is a Unittest for max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegers(unittest.TestCase):
    """Suite test for max_integer function"""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_float_numbers(self):
        self.assertEqual(max_integer([0.5, 0.9, 100.50, 100.51]), 100.51)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-50, -5, -90, -3]), -3)

    def test_large_list(self):
        self.assertEqual(max_integer([
            901, 902, 903, 904, 905, 906, 907, 908, 909, 910,
            911, 912, 913, 914, 915, 916, 917, 918, 919, 920,
            919, 918, 917, 1000, 915, 914, 913, 912, 911, 910,
            909, 908, 907, 906, 905, 904, 903, 902, 901]), 1000)

    def test_operated_list(self):
        self.assertEqual(max_integer([2 + 3, 5 * 2, 6 - 3, 50 / 10]), 10)

    def test_one_number(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)

# def max_integer(list=[]):
#     """Function to find and return the max integer in a list of integers
#         If the list is empty, the function returns None
#     """
#     if len(list) == 0:
#         return None
#     result = list[0]
#     i = 1
#     while i < len(list):
#         if list[i] > result:
#             result = list[i]
#         i += 1
#     return result
