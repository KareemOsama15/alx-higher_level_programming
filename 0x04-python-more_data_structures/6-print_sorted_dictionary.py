#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newLsit = []
    for key in a_dictionary:
        newLsit.append(key)
    for item in sorted(newLsit):
        print("{}: {}".format(item, a_dictionary[item]))
