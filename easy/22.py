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


class Fib:

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a

        if self.i > self.n:
            raise StopIteration

        self.a, self.b = self.b, self.a + self.b
        self.i += 1
        return fib


with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        fib = 0
        for x in Fib(int(line)):
            fib = x
        print(fib)