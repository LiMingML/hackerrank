#!/bin/python3

import math
import os
import random
import re
import sys
from math import gcd
from functools import reduce


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# LCM: least common multiple，最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)

# GCD: greatest common divisor，最大公约数
def get_lcm(arr):
    return reduce(lcm, arr, 1)


def get_gcd(arr):
    return reduce(gcd, arr)


def getTotalX(a, b):
    # Write your code here

    lcm_a = get_lcm(a)
    gcd_b = get_gcd(b)
    if gcd_b % lcm_a != 0:
        return 0

    target = gcd_b // lcm_a
    count = 0
    for i in range(1, int(math.sqrt(target)) + 1):
        if target % i == 0:
            if i == target // i:
                count += 1
            else:
                count += 2
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
