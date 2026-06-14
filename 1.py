import numpy as np

# Matrix exponentiation
n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

k = int(input())

a = np.array(matrix)
result = np.linalg.matrix_power(a, k)

for row in result:
    print(*row)                 


# Matrix multiplication
n, m = map(int, input().split())
matrix_a = []
matrix_b = []
for i in range(n):
    matrix_a.append(list(map(int, input().split())))
input()   

k, l = map(int, input().split())
for i in range(k):
    matrix_b.append(list(map(int, input().split())))
a, b = np.array(matrix_a), np.array(matrix_b)

result = a @ b

for row in result:
    print(*row)


# Matrix addition
n, m = map(int, input().split())

matrix_a = []
matrix_b = []

for i in range(n):
    matrix_a.append(list(map(int, input().split())))
input()    
for i in range(n):
    matrix_b.append(list(map(int, input().split())))
       
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    print(*row)

