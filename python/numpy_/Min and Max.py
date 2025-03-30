import numpy as np

n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)

row_min = np.min(arr, axis=1)
print(np.max(row_min))