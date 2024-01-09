#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    j = 0
    for i in range(1, len(sys.argv)):
        j += 1
    
    if j == 0:
        print("{} arguements.".format(j))
    elif j == 1:
        print(f"{j} arguement:\n{j}: {sys.argv[1]}")
    else:
        print(f"{j} arguement:")
        for i in range(1, j+1):
            print(f"{i}: {sys.argv[i]}")
