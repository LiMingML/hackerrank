#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    """
    Brute force
    :param s:
    :return:
    """
    # Write your code here
    # All possible 3x3 magic squares
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    min_cost = float('inf')

    for magic in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(s[i][j] - magic[i][j])
        if cost < min_cost:
            min_cost = cost

    return min_cost

def formingMagicSquare2(s):
    """
    Key Observations:
    1. The center of a 3×3 magic square must be 5
    2. The four corners must be even numbers (2,4,6,8)
    3. The edge centers must be odd numbers (1,3,7,9)
    4. The magic constant (sum of each row/column/diagonal) is always 15
    :param s:
    :return:
    """
    # Write your code here
    # The center must be 5 - if not, we must modify it
    cost = abs(s[1][1] - 5)
    s[1][1] = 5  # Set directly to 5 as this is mandatory

    # Predefined corner and edge patterns
    corner_patterns = [
        [8, 6, 2, 4],
        [6, 8, 4, 2],
        [4, 2, 8, 6],
        [2, 4, 6, 8]
    ]
    edge_patterns = [
        [1, 7, 9, 3],
        [3, 9, 7, 1],
        [7, 1, 3, 9],
        [9, 3, 1, 7]
    ]

    min_total_cost = float('inf')

    # Only need to check 4 base patterns (the other 4 are mirrors)
    for i in range(4):
        # Calculate corner cost
        corners = [s[0][0], s[0][2], s[2][2], s[2][0]]
        corner_cost = sum(abs(corners[j] - corner_patterns[i][j]) for j in range(4))

        # Calculate edge cost
        edges = [s[0][1], s[1][2], s[2][1], s[1][0]]
        edge_cost = sum(abs(edges[j] - edge_patterns[i][j]) for j in range(4))

        total_cost = cost + corner_cost + edge_cost
        if total_cost < min_total_cost:
            min_total_cost = total_cost

    return min_total_cost
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
