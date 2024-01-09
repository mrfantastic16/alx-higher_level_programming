#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
a = 10
b = 5
calc_lst = [add, sub, mul, div]
sign = ['+', '-', '*', '/']

for i in range(len(calc_lst)):
    print("{} {} {} = {}".format(a, sign[i], b, calc_lst[i](a, b)))
