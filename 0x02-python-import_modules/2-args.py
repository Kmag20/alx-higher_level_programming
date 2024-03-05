#!/usr/bin/python3

if __name__ == '__main__':
    """ prints the number of and list of args """
    import sys

    if len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
    elif len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv) - 1))

    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if i > 0:
                print("{}: {}".format(i, arg))
