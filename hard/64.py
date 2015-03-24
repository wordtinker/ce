"""
Climbing Stairs
Challenge Description:
You are climbing a stair case. It takes n steps to reach to the top. Each time
you can either climb 1 or 2 steps. In how many distinct ways can you climb to
the top?
Input sample:
10
20
Your program should accept as its first argument a path to a filename. Each line
in this file contains a positive integer which is the total number of stairs.
Ignore all empty lines. E.g.
Output sample:
89
10946
Print out the number of ways to climb to the top of the staircase. E.g.
Constraints:
The total number of stairs is <= 1000

Solution calculates the number of combinations for each subset of 1 and 2 that
represents the given number of steps

"""

from sys import argv
from math import factorial

def combs(k, n):
    return factorial(n) // factorial(k) // factorial(n - k)

def _combs(k, n):  # Gives no more speed
    """
      n!      n(n-1)...(n-r+1)
--------- = ----------------
 r!(n-r)!          r!

    and furter
    n / 1 * (n-1) / 2 * (n-2) / 3 * ... * (n-r+1) / r
    """
    upper = 1
    lower = 1
    for u, l in zip(range(n, n - k, -1), range(1, k + 1)):
        upper *= u
        lower *= l

    return upper // lower


def split(steps):
    return steps // 2, steps % 2


with open(argv[1]) as file:   # Keep it for CodeEval
    for line in file:
        steps = int(line)
        long, short = split(steps)
        combinations = 0
        while long >= 0:
            combinations += combs(short, short + long)
            long -= 1
            short += 2
        print(combinations)


# def test_factorial():
#     for i in range(1):
#         combs(10, 50)
#
# def test_zip():
#     for i in range(1):
#         _combs(10, 50)
#
# if __name__ == "__main__":
#     import timeit
#     print(timeit.timeit("test_factorial()",
#                         setup="from __main__ import test_factorial"))
#     print(timeit.timeit("test_zip()",
#                         setup="from __main__ import test_zip"))
