#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            cAscii = ord(str[i]) - 32
        else:
            cAscii = ord(str[i])
        print("{:c}".format(cAscii), end='')
    print()
