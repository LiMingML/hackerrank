import numpy as np

n, m = map(int, input().split())

# Read array A
A = np.array([input().split() for _ in range(n)], int)
# Read array B
B = np.array([input().split() for _ in range(n)], int)

# Perform operations
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
