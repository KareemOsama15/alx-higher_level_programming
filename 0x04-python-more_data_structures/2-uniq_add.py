#!/usr/bin/python3

def uniq_add(my_list=[]):
    newLsit = set(my_list)
    sum = 0
    for num in newLsit:
        sum += num
    return (sum)
