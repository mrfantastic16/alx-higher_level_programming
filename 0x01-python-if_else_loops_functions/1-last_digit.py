#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
output = "Last digit of {} is {} and is {}"

if number < 0:
    last_digit = -((-number) % 10)
else:
    last_digit = number % 10

if last_digit > 5:
    print(output.format(number, last_digit, "greater than 5"))
elif (last_digit < 6) and (last_digit != 0):
    print(output.format(number, last_digit, "less than 6 and not 0"))
else:
    print(output.format(number, last_digit, "0"))
