#!/usr/bin/python3

if __name__ == '__main__':
        """ Import all funcs of the calculator_1 and handles basic operations """
        from calculator_1 import add, sub, mul, div
        import sys

        if len(sys.argv) - 1 != 3:
                print("Usage: /100-my_calculator.py <a> operator <b>")
                sys.exit(1)

        operator = sys.argv[2]

        if operator == '+':
            result = add(int(sys.argv[1]), int(sys.argv[3]))
        elif operator == '-':
            result = sub(int(sys.argv[1]), int(sys.argv[3]))
        elif operator == '*':
            result = mul(int(sys.argv[1]), int(sys.argv[3]))
        elif operator == '/':
            result = div(int(sys.argv[1]), int(sys.argv[3]))
        else:
                print("Unknown operator: Available operators: +, -, *, and /")
                sys.exit(1)

        print("{} {} {} = {}".format(sys.argv[1], operator, sys.argv[3], result))
        sys.exit(0)