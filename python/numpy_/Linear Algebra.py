import numpy as np

n = int(input())
matrix = np.array([input().split() for _ in range(n)], float)

det = np.linalg.det(matrix)
print(round(det, 2))