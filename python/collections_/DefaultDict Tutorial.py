# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m = map(int,input().split())

a = defaultdict(list)

for i in range(n):
    a[input()].append(i+1)

for i in range(m):
    print(*a[x] if (x:=input()) in a else [-1])
