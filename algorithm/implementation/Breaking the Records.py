#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    most_cnt, least_cnt = 0, 0
    most_base, least_base = scores[0], scores[0]
    for score in scores:
        if score > most_base:
            most_cnt += 1
            most_base = score
        if score < least_base:
            least_cnt += 1
            least_base = score
    return [most_cnt, least_cnt]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
