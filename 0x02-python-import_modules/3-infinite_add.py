#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    i = 0

    for j in range(1, len(argv)):
        i += int(argv[j])

    print(i)
