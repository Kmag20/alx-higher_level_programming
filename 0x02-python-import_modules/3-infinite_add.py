#!/usr/bin/python3

if __name__ == '__main__':
    """ prints the results of the addition of all args """
    import sys

    sum = 0
    for i, arg in enumerate(sys.argv):
        if i > 0:
            sum += int(arg)

    print(sum)
