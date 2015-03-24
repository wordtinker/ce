"""
Write a program which checks input numbers and determines whether a number is
even or not.
"""

import sys

with open(sys.argv[1]) as file:
    for test in file:
        i = int(test)
        r = '1' if i % 2 == 0 else '0'
        print(r)