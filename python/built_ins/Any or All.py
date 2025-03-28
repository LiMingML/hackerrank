n = int(input())
lst = list(map(int, input().split()))
print(all(i>0 for i in lst) and any(str(i)[::-1]==str(i) for i in lst))
