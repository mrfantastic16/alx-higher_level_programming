#!/usr/bin/python3

for i in range(0, 9):
    for j in range(i+1, 10):
        if not (i == 8 and j == 9):
            print("{0:d}{1:d}".format(i, j), end=", ")
        else:
            print("{0:d}{1:d}".format(i, j))
