#!/usr/bin/python3

def safe_print_division(a, b):
    """ Divides 2 integers and prints the result """
    try:
        m = a / b
    except (ZeroDivisionError, TypeError):
        m = None
    finally:
        print('Inside result: {}'.format(m))
    return m
