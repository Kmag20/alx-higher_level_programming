#!/usr/bin/python3
# Python script that takes in a URL, sends a request
# to the URL and displays the value of the X-Request-Id
# variable found in the header of the response.

import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as response:
    headers = response.info()
    for var, val in headers._headers:
        if var == 'X-Request-Id':
            x_request_id = val
            break

    if x_request_id is None:
        print('X-Request-Id header not found')
    else:
        print(x_request_id)
