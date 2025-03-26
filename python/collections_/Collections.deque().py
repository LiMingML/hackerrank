# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque


N = int(input())
d = deque()
for _ in range(N):
    name_para = input().split()
    if len(name_para) == 1:
        getattr(d, name_para[0])()
    if len(name_para) == 2:
        getattr(d, name_para[0])(int(name_para[1]))
print(*d)
