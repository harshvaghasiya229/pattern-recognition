print("IAR/17360")

import numpy as np

# Create two 3 x 3 matrices
A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

B = np.array([[2, 1, 0],
              [1, 3, 2],
              [4, 0, 1]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Addition
print("\nAddition of A and B:")
print(A + B)

# Subtraction
print("\nSubtraction of A and B:")
print(A - B)

# Element-wise multiplication
print("\nElement-wise multiplication:")
print(A * B)

# Matrix multiplication
print("\nMatrix multiplication:")
print(np.dot(A, B))

# Transpose of A
print("\nTranspose of A:")
print(A.T)

# Determinant of A
print("\nDeterminant of A:")
print(np.linalg.det(A))

# Inverse of A
print("\nInverse of A:")
print(np.linalg.inv(A))

# Solve equations: 2x + y = 5 and x + 3y = 10
# Matrix form: AX = B
coefficients = np.array([[2, 1],
                         [1, 3]])

values = np.array([5, 10])

answer = np.linalg.solve(coefficients, values)

print("\nSolution of equations:")
print("x =", answer[0])
print("y =", answer[1])
