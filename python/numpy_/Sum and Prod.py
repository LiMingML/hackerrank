import numpy as np

n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)

sum_axis0 = np.sum(arr, axis=0)
print(np.prod(sum_axis0))