#!/usr/bin/python3

def main():
    if __name__ == '__main__':
        from calculator_1 import add, sub, mul, div
        from sys import argv, exit

        a_operators = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
            }

        if len(argv) != 4:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)

        operand_1 = int(argv[1])
        operand_2 = int(argv[3])
        op = (argv[2])

        result = a_operators[op](operand_1, operand_2)
        print(f"{operand_1} {op} {operand_2} = {result}")


def check_op(op):
    if op not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


main()
