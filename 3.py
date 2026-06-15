#Fill in the code to find the vertex of a parabola given its coefficients a, b, and c

def parabola_vertex(a, b, c):
    x0 = -b / (2 * a)
    y0 = (4 * a * c - b ** 2) / (4 * a)
    return (x0, y0)


print(parabola_vertex(int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: "))))



#Fill in the code to find good students with grades above 3
students = [tuple(input().split() for _ in range(int(input("Enter number of students: "))))]

for student in students:
    print(student)

print()

for name, grade in students:
    if int(grade) > 3:
        print(name, grade)


#fill in the code to find the first n numbers in the Tribonacci sequence
n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end = ' ')
    f1, f2, f3 = f3, f3 + f2 + f1, f2




       