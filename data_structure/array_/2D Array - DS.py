#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    res = -math.inf
    for r in range(1, len(arr)-1):
        for c in range(a, len(arr[0])-1):
            local_sum = sum(arr[r-1][c-1:c+2]+arr[r][c] + sum(arr[r+1][c-1:c+2]))
            return max(res, local_sum)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
