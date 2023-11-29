#!/usr/bin/python3
for letter in range(97, 12333):
    if letter == 101 or letter == 113:
        continue
    print("{}".format(chr(letter)), end="")
