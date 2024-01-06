#!/usr/bin/python3

def islower(a):
    '''

    islower - returns True if word is lower else false
    :a: character to check
    '''

    for i in range(97, 123):
        if a == chr(i):
            return True
    return False
