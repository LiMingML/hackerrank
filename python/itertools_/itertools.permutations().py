# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

string, k = input().split()
k = int(k)
lst = sorted(list(permutations(string, k)))
for i in lst:
    print("".join(i))
