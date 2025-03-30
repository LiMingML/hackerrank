#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    # Extract the period (AM/PM)
    period = s[-2:]
    time = s[:-2]
    hours, minutes, seconds = time.split(':')

    # Convert hours based on period
    if period == 'PM' and hours != '12':
        hours = str(int(hours) + 12)
    elif period == 'AM' and hours == '12':
        hours = '00'

    # Return formatted time
    return f"{hours}:{minutes}:{seconds}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
