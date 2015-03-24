"""
Multiply Lists

Challenge Description:

You have 2 lists of positive integers. Write a program which multiplies
corresponding elements in these lists.
Input sample:

Your program should accept as its first argument a path to a filename.
Input example is the following

9 0 6 | 15 14 9
5 | 8
13 4 15 1 15 5 | 1 4 15 14 8 2

The lists are separated with a pipe char, numbers are separated with a space char.
The number of elements in lists are in range [1, 10].
The number of elements is the same in both lists.
Each element is a number in range [0, 99].
Output sample:

Print the result in the following way.

135 0 54
40
13 16 225 14 120 10
"""

from sys import argv

with open(argv[1]) as file:
    for test in file:
        list1, list2 = test.split('|')
        result = []
        for i, j in zip(list1.split(), list2.split()):
            result.append(int(i) * int(j))
        print(' '.join(str(i) for i in result))