""" Write a program which determines the number of 1 bits in the internal
representation of a given integer.
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print(str(bin(int(test))).count('1'))
