#!/usr/bin/python3
""" Takes in a URL and email and sends in a POST request """

import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
values = {'email':  sys.argv[2]}

data = urllib.parse.urlencode(email).encode('ascii')
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
    print(response.read().decode('utf-8'))
