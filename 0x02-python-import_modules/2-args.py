#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    arg_len = len(sys.argv) - 1

    if arg_len == 0:
        print("0 arguments.")
    elif arg_len == 1:
        print("1 argument:")
    else:
        print(f"{arg_len} arguments:")

    for i, v in enumerate(sys.argv[1:]):
        print(f"{i + 1}: {v}")
