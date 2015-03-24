"""
Challenge Description:

In chess, the knight moves to any of the closest squares that are not on the
same rank, file, or diagonal. Thus the move is in the “L” form: two squares
vertically and one square horizontally, or two squares horizontally and one
square vertically:

Your task is to find all possible positions for the next move of the knight on
the empty chessboard.
Input sample:

The first argument is a filename that contains positions of the knight on the
chessboard in the CN form, where:

    C is a letter from “a” to “h” and denotes a column.
    N is a number from 1 to 8 and denotes a row.

Each position is indicated in a new line.

For example:
Output sample:

Print to stdout all possible positions for the next move of the knight ordered alphabetically.

For example:
Constraints:

    The number of test cases is 40.

"""


import sys


def legal_coord(x):
    return 0 <= x < 8


def get_legal_moves(row, col):
    new_moves = []
    offsets = ((-1, -2), (-1, 2), (-2, -1), (-2, 1),
              (1, -2), (1, 2), (2, -1), (2, 1))

    for i, j in offsets:
        if legal_coord(row + i) and legal_coord(col + j):
            new_moves.append((row + i, col + j))

    return new_moves

def get_moves(pos):
    r = ord(pos[0]) - 97
    c = int(pos[1]) - 1
    new_moves = [chr(97 + i) + str(j + 1) for i, j in get_legal_moves(r, c)]
    return new_moves

with open(sys.argv[1]) as file:
    for line in file:
        print(' '.join(sorted(get_moves(line))))