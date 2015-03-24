"""
 Given a list of numbers and a positive integer k, reverse the elements of the
list, k items at a time. If the number of elements is not a multiple of k, then
the remaining items in the end should be left as is.
Input sample:
Your program should accept as its first argument a path to a filename. Each line
in this file contains a list of numbers and the number k, separated by a
semicolon. The list of numbers are comma delimited. E.g.
1,2,3,4,5;2
1,2,3,4,5;3

Output sample:
Print out the new comma separated list of numbers obtained after reversing. E.g.

2,1,4,3,5
3,2,1,4,5
"""

import sys


def revers(array, start, length):
    for i in range(length // 2):
        j = start + i
        k = length + start - i - 1
        array[k], array[j] = array[j], array[k]


with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        arr, shift = line.split(';')
        arr = arr.split(',')
        shift = int(shift)
        length = len(arr)
        for i in range(0, length, shift):
            if i + shift <= length:
                revers(arr, i, shift)
        print(','.join(arr))

# x = [1,2,3,4,5,6,7,8,9]
# revers(x,2,4)
# print(x)