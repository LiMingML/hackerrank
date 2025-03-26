# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s_n = set(map(int, input().split()))
b = int(input())
s_b = set(map(int, input().split()))
print(len(s_n.difference(s_b)))
