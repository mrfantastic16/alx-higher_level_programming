#!/usr/bin/python3

def print_last_digit(number):
    ld = number % 10 if number >= 0 else (number * -1) % 10
    print(ld, end="")
    return ld
