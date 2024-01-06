#!/usr/bin/python3

def islower(a):
    '''

    islower - returns True if word is lower else false
    :a: character to check
    '''
    if ord(a) in list(range(97, 123)):
        return True
    else:
        return False
