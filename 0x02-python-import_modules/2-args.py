#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

    j = len(argv) - 1
    
    if j == 0:
        print(f"{j} arguments.")
    elif j == 1:
        print(f"{j} argument:\n{j}: {argv[1]}")
    else:
        print(f"{j} arguments:")
        for i in range(1, j+1):
            print(f"{i}: {argv[i]}")
