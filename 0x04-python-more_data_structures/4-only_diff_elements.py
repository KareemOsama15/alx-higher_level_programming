#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    newSet = set()

    for item1 in set_1:
        if item1 not in set_2:
            newSet.add(item1)
    for item2 in set_2:
        if item2 not in set_1:
            newSet.add(item2)
    return (newSet)
    # return (set_1 ^ set_2)
