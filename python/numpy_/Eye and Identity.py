import numpy as np

np.set_printoptions(legacy='1.13')  # This is to match Hackerrank's output format

n, m = map(int, input().split())
print(np.eye(n, m))