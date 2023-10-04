#!/usr/bin/python3

def islower(c):
    c = ord(c)
    for cAscii in range(97, 123):
        if c == cAscii:
            return(True)
    if c != cAscii:
        return(False)
