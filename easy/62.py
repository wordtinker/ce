"""
N MOD M
CHALLENGE DESCRIPTION:

Given two integers N and M, calculate N Mod M (without using any inbuilt modulus operator).

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains two comma separated positive integers. E.g.

20,6
2,3
You may assume M will never be zero.

OUTPUT SAMPLE:

Print out the value of N Mod M
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        n, d = line.split(',')
        n, d = int(n), int(d)
        whole = n // d
        modulus = n - whole * d
        print(modulus)