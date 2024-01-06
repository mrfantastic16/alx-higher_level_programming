#!/usr/bin/python3

def uppercase(str):
    '''

    uppercase: converts lowercase characters to uppercase
    :str: string or phrase passed in
    '''

    for st in str:
        if ord(st) in list(range(97, 123)):
            print("{}".format(chr(ord(st) - 32)), end='')
        else:
            print("{}".format(st), end='')
