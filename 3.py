def parabola_vertex(a, b, c):
    x0 = -b / (2 * a)
    y0 = (4 * a * c - b ** 2) / (4 * a)
    return (x0, y0)


print(parabola_vertex(int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: "))))