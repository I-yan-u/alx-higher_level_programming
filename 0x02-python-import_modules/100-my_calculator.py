#!/usr/bin/python3
if __name__ == '__main__':
    from sys import exit, argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = ['+', '-', '*', '/']
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if op == '+':
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
        elif op == '-':
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
        elif op == '*':
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))
        else:
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
