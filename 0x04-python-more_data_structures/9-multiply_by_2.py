#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDict = {}
    for item in a_dictionary:
        newDict[item] = a_dictionary[item] * 2
    return (newDict)
