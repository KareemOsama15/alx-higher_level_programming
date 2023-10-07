#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    checkList = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            checkList.append(True)
        else:
            checkList.append(False)
    return (checkList)
