#!/usr/bin/python3
# Python script that takes in a URL, sends a request

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(dict(response.headers).get('X-Request-Id'))
