#!/usr/bin/python3
"""
Sends a req to a URL and handles the response and also
the error
"""
import urllib.error
import urllib.request
import sys

url = sys.argv[1]
req = urllib.request.Request(url)

try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('ascii'))
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))
