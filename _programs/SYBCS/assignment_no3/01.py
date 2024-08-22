from sympy import *

A = Matrix([[2,3,4],[5,4,3],[7,8,5]])

print(A)

# Matrix([[2, 3, 4], [5, 4, 3], [7, 8, 5]])

B = Matrix([[2,4,6],[6,5,8],[9,7,4]])

print(B)

# Matrix([[2, 4, 6], [6, 5, 8], [9, 7, 4]])

print(A+B)

# Matrix([[4, 7, 10], [11, 9, 11], [16, 15, 9]])

print(A.det())

# o/p:- 28

print(B.det())

# o/p:- 102

print(A.inv())

# Matrix([[-1/7, 17/28, -1/4], [-1/7, -9/14, 1/2], [3/7, 5/28, -1/4]])

print(B.inv())

# Matrix([[-6/17, 13/51, 1/51], [8/17, -23/51, 10/51], [-1/34, 11/51, -7/51]])

print(A.T)

# Matrix([[2, 5, 7], [3, 4, 8], [4, 3, 5]])

print(B.T)

# Matrix([[2, 6, 9], [4, 5, 7], [6, 8, 4]])

print(A.row(1))

# Matrix([[5, 4, 3]])

print(B.col(1))

# Matrix([[4], [5], [7]])

print(A.rref())

# (Matrix([
# [1, 0, 0],
# [0, 1, 0],
# [0, 0, 1]]), (0, 1, 2))

B.row_del(1)
print(B)

# Matrix([[2, 4, 6], [9, 7, 4]])

print(A.rank())

# o/p:- 3

print(ones(3))

# Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

print(diag(1,2,5))

# Matrix([[1, 0, 0], [0, 2, 0], [0, 0, 5]])

print(zeros(3))

# Matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

print(A**2)

# Matrix([[47, 50, 37], [51, 55, 47], [89, 93, 77]])