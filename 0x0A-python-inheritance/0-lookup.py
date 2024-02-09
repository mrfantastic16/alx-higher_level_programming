#!/usr/bin/python3
'''Defines an object attribute lookup function'''


def lookup(obj):
    ''' Returns a list available attr and methods '''
    return dir(obj)
