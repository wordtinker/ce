"""
FIBONACCI SERIES
CHALLENGE DESCRIPTION:

The Fibonacci series is defined as: F(0) = 0; F(1) = 1; F(n) = F(n–1) + F(n–2) when n>1. Given an integer n≥0, print out the F(n).

INPUT SAMPLE:

The first argument will be a path to a filename containing integer numbers, one per line. E.g.

5
12
OUTPUT SAMPLE:

Print to stdout, the fibonacci number, F(n). E.g.

5
144
"""
import sys

dic = {}


def fib(n: int) -> int:
    """
    Memoized and recursive
    Returns n'th fibonaci number
    """

    if n not in dic:
        if n == 1:
            f = 0
        elif n == 2:
            f = 1
        else:
            f = fib(n-1) + fib(n-2)

        dic[n] = f

    return dic[n]

with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        print(fib(int(line)))
