"""
Valid parentheses

Challenge Description:

Given a string comprising just of the characters (,),{,},[,] determine if it is
well-formed or not.
Input sample:

Your program should accept as its first argument a path to a filename. Each line
 in this file contains a string comprising of the characters mentioned above.
  E.g.

()
([)]

Output sample:

Print out True or False if the string is well-formed. E.g.

True
False
"""

import sys

parenthesis = {
    '(': ')',
    '{': '}',
    '[': ']'
}


def is_valid(string: str) -> bool:
    stack = []

    for elem in string:
        if elem in parenthesis:
            stack.append(elem)
        elif len(stack) == 0 or parenthesis[stack.pop()] != elem:
            return False
    else:
        return len(stack) == 0

with open(sys.argv[1]) as file:
    for test in file:
        print(is_valid(test.rstrip()))