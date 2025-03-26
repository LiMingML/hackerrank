# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())
X_list = list(map(int, input().split()))
N = int(input())

shoe_size = Counter(X_list)
earn = 0
for i in range(N):
    size, amount = tuple(map(int, input().split()))
    if size in shoe_size.keys() and shoe_size[size] != 0:
        shoe_size[size] -= 1
        earn += amount

print(earn)

