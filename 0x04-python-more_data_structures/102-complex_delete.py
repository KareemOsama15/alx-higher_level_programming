#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    newList = list(a_dictionary.keys())

    for item in newList:
        if value == a_dictionary[item]:
            del a_dictionary[item]
    return (a_dictionary)
