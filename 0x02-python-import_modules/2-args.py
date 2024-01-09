#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    j = 0
    for i in range(1, len(argv)):
        j += 1
    
    if j == 0:
        print(f"{j} arguements.")
    elif j == 1:
        print(f"{j} arguement:\n{j}: {argv[1]}")
    else:
        print(f"{j} arguement:")
        for i in range(1, j+1):
            print(f"{i}: {argv[i]}")
