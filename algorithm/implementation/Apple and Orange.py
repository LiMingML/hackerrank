#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    """

    :param s: staring point of the house
    :param t: end point of the house
    :param a: location of the apple tree
    :param b: location of the orange tree
    :param apples: distance of the apples falls from the tree
    :param oranges: distance of the oranges falls from the tree
    :return:
    """
    # Write your code here
    apples_distance = [i + a for i in apples]
    orange_distance = [i + b for i in oranges]
    cnt = 0
    for i in apples_distance:
        if s <= i <= t:
            cnt += 1
    print(cnt)
    cnt = 0
    for i in orange_distance:
        if s <= i <= t:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
