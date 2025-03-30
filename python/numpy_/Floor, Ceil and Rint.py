import numpy as np

np.set_printoptions(legacy='1.13')  # To match Hackerrank's output format

A = np.array(input().split(), float)

print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))
