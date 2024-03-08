#!/usr/bin/ python3

def print_reverse_list_integer(my_list=[]):
    """ print all integers of a list """
    if isinstance(my_list, list):
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(i))

