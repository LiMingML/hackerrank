# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

d = OrderedDict()
N = int(input())
for _ in range(N):
    name, price = input().rsplit(" ", 1)
    price = int(price)
    if name in d:
        d[name] += price
    else:
        d[name] = price
for k, v in d.items():
    print(k, v)

