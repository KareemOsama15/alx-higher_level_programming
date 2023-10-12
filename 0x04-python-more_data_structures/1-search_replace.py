#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newList = []
    for i in range(len(my_list)):
        newList.append(my_list[i])
        if newList[i] == search:
            newList[i] = replace
    return (newList)
