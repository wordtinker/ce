"""
Prefix expressions

Challenge Description:

You are given a prefix expression. Write a program which evaluates it.

Your program should accept a file as its first argument. The file contains one
prefix expression per line.

For example: * + 2 3 4

Your program should read this file and insert it into any data structure you
like. Traverse this data structure and evaluate the prefix expression. Each
token is delimited by a whitespace. You may assume that sum ‘+’, multiplication
‘*’ and division ‘/’ are the only valid operators appearing in the test data.

Print to stdout the output of the prefix expression, one per line.

For example: 20
Constraints:

    The evaluation result will always be an integer ≥ 0.
    The number of the test cases is ≤ 40.


The solution is build on simple stack.
"""

import sys
import operator
from math import ceil

operations = {
    '+': operator.add,
    '*': operator.mul,
    '/': operator.truediv
}


with open(sys.argv[1]) as file:
    for test in file:
        expression = test.rstrip().split()
        stack = []
        for elem in reversed(expression):
            if elem in operations:
                a = stack.pop()
                b = stack.pop()
                stack.append(operations[elem](a, b))
            else:
                stack.append(int(elem))
        print(int(ceil(stack.pop())))
