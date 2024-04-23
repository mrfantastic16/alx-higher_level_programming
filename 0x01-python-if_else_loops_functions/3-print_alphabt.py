#!/usr/bin/python3

for j in range(97, 123):
    if chr(j) == 'q' or chr(j) == 'e':
        continue
    print("{}".format(chr(j)), end="")
