"""
You are given two sorted list of numbers (ascending order). The lists themselves
are comma delimited and the two lists are semicolon delimited. Print out the
intersection of these two sets.
"""
import sys

with open(sys.argv[1]) as file:
    for test in file:
        set1, set2 = test.split(';')
        set1 = {int(i) for i in set1.split(',')}
        set2 = {int(i) for i in set2.split(',')}
        print(','.join(str(i) for i in sorted(set1.intersection(set2))))