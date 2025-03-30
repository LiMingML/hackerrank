import numpy


n, m, p = map(int, input().split())
arr1,arr2 = [], []
for _ in range(n):
    arr1.append(list(map(int, input().split())))
for _ in range(m):
    arr2.append(list(map(int, input().split())))

a1 = numpy.array(arr1)
a2 = numpy.array(arr2)
a = numpy.concatenate((a1, a2))
print(a)
