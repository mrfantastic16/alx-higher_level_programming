#!/usr/bin/python3

def uppercase(str):
    '''

    uppercase: converts lowercase characters to uppercase
    :str: string or phrase passed in
    '''
    upper = []

    for st in str:
        if ord(st) in list(range(97, 123)):
            upper.append(chr(ord(st) - 32))
        else:
            upper.append(st)

    for up in upper:
        print("{}".format(up), end='')
    print()
