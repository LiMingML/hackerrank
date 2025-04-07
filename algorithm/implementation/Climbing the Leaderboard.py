#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    """
    According to the description, we do not need to insert the score into ranked list.
    :param ranked:
    :param player:
    :return:
    """
    # Write your code here
    unique_sorted = sorted(list(set(ranked)), reverse=True)

    result = []
    for score in player:
        left, right = 0, len(unique_sorted)
        # Binary search to find the insertion point
        while left < right:
            mid = (left + right) // 2
            if unique_sorted[mid] > score:
                left = mid + 1
            else:
                right = mid
        result.append(left + 1)
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # ranked_count = int(input().strip())
    #
    # ranked = list(map(int, input().rstrip().split()))
    #
    # player_count = int(input().strip())
    #
    # player = list(map(int, input().rstrip().split()))
    #
    # result = climbingLeaderboard(ranked, player)
    #
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
    ranked_count = 7
    ranked = list(map(int, '100 100 50 40 40 20 10'.split()))
    player_count = 4
    player = list(map(int, '5 25 50 120'.split()))
    result = climbingLeaderboard(ranked, player)
    print(result)
