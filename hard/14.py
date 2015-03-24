"""
String Permutations

Challenge Description:
Write a program which prints all the permutations of a string in alphabetical
order. We consider that digits < upper case letters < lower case letters. The
sorting should be performed in ascending order.
Input sample:
Your program should accept a file as its first argument. The file contains
input strings, one per line.

For example:
hat
abc
Zu6
Output sample:

Print to stdout the permutations of the string separated by comma, in
alphabetical order.

For example:
aht,ath,hat,hta,tah,tha
abc,acb,bac,bca,cab,cba
6Zu,6uZ,Z6u,Zu6,u6Z,uZ6
"""
import sys


def permute(left, right="", result=[]):
    if len(left) == 0:
        result.append(right)
    else:
        for i, letter in enumerate(left):
            permute(left[:i]+left[i + 1:], letter + right, result)

    return sorted(result)


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print(','.join(permute(test.rstrip(), '', [])))