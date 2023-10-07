#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < len(my_list) and idx >= 0:
        for i in my_list:
            if i == idx:
                my_list[i] = element
                break
        return (my_list)
    else:
        return (my_list)
