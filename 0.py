#Fill the matrix with numbers from 1 to n*m
n, m = map(int, input().split())
           
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(i * m + j + 1)
    matrix.append(row)


for row in matrix:
    print(*row)


#Fill the matrix with numbers from 1 to n*m in column-wise order
n, m = map(int, input().split())
size = n * m           
matrix = []

for i in range(1, n + 1):
    row = []
    for j in range(i, size + 1, n):
        row.append(j)
    matrix.append(row)



for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()




#Fill the matrix with 1s on the main diagonal and the anti-diagonal, and 0s elsewhere
n = int(input())

matrix = []
for i in range(n):
    matrix.append([0] * n)

for i in range(n):
    for j in range(n):
        if i == j or i + j + 1 == n:
            matrix[i][j] = 1
    
for row in matrix:
    print(*row)



#Fill the matrix with 1s on the main diagonal, the anti-diagonal, and the areas above and below them, and 0s elsewhere
n = int(input())

matrix = []
for i in range(n):
    matrix.append([0] * n)

for i in range(n):
    for j in range(n):
        if i == j or i + j + 1 == n:
            matrix[i][j] = 1
        elif i > j and i + j + 1 > n or i < j and i + j + 1 < n:
            matrix[i][j] = 1
    
for row in matrix:
    print(*row)


#Fill the matrix with numbers from 1 to m in a cyclic manner, where m is the number of columns
n, m = map(int, input().split())

matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append((i + j) % m + 1)
    matrix.append(row)
        
             
            
        
for row in matrix:
    print(*row)



#Fill the matrix with numbers from 1 to n*m in a zigzag manner, where the first row is filled from left to right, the second row is filled from right to left, and so on (Snake-method)
n, m = map(int, input().split())

matrix = []
count = 0

for i in range(n):
    row = []
    for j in range(m):
        count += 1
        row.append(count)
    matrix.append(row)
    

count = 0

for row in matrix:
    if count % 2 == 0:
        print(*row)
    else:
        print(*row[::-1])
    count += 1


#Fill the matrix with numbers from 1 to n*m in a diagonal manner, where the first diagonal (from the top-left corner) is filled with 1, the second diagonal is filled with 2, and so on
n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]

nm = 0

for q in range(n*m):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                nm += 1
                matrix[i][j] = nm
        
for row in matrix:
    print(*row)



#Fill the matrix with numbers from 1 to n*m in a spiral manner, where the first number is placed in the top-left corner, and the numbers are filled in a clockwise direction
n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]

top, bottom, left, right = 0, n - 1, 0, m - 1
num = 1

while top <= bottom and left <= right:
    # → вправо по верхньому рядку
    for j in range(left, right + 1):
        matrix[top][j] = num
        num += 1
    top += 1

    # ↓ вниз по правому стовпцю
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    # ← вліво по нижньому рядку
    if top <= bottom:
        for j in range(right, left - 1, -1):
            matrix[bottom][j] = num
            num += 1
        bottom -= 1

    # ↑ вверх по лівому стовпцю
    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

for row in matrix:
    print(*[str(x).ljust(3) for x in row])


