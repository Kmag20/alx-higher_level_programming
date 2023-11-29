#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 == 0:
        print(f"{chr(letter)}", end="")

    else:
        print(f"{chr(letter - 32)}", end="")
