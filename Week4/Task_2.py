#Task 2:
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[7, 8],
     [9, 10],
     [11, 12]]
result = [[0, 0],
          [0, 0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
print("Matrix A:")
for row in A:
    print(row)
print("\nMatrix B:")
for row in B:
    print(row)
print("\nResult of Matrix Multiplication (A x B):")
for row in result:
    print(row)