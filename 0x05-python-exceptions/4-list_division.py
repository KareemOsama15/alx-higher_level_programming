#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    newList = []
    i = 0
    while i < list_length:
        try:
            result = my_list_1[i] / my_list_2[i]
        # handle if index type was a string or any other type just int
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:   # handle divide on 0
            result = 0
            print("division by 0")
        except IndexError:  # handle if x > length of any list
            result = 0
            print("out of range")
        finally:
            newList.append(result)
        i += 1
    return newList
