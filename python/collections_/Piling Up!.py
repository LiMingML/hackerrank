# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
import sys

T = int(input())
for _ in range(T):
    n = int(input())
    cubes = deque(map(int, input().split()))
    lst = [sys.maxsize]

    flag = "Yes"
    while len(cubes):
        if cubes[0] > cubes[-1]:
            if cubes[0] > lst[-1]:
                flag = "No"
                break
            else:
                lst.append(cubes.popleft())
        else:
            if cubes[-1] > lst[-1]:
                flag = "No"
                break
            else:
                lst.append(cubes.pop())
    print(flag)


