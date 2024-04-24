#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    print(sum([int(n) for n in argv[1:]]))
