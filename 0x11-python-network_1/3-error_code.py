#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
(handling HTTP errors)import urllib.error
"""
import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)

try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('ascii'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
