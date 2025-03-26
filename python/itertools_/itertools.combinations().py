# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

string, k = input().split()
string = sorted(string)
k = int(k)

for i in range(1, k + 1):
    lst = list(combinations(string, i))

    for j in lst:
        print("".join(j))

