#!/usr/bin/python3

i = 0

for j in range(122, 96, -1):
    print("{}".format(chr(j) if i % 2 == 0 else chr(j - 32)), end="")
    i += 1
