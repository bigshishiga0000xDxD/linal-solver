from matrix import *

def transform1(a: Matrix, i, j, x):
    if i == j:
        raise Exception

    for k in range(a.m):
        a.a[i][k] += a.a[j][k] * x


def transform2(a: Matrix, i, j):
    a.a[i], a.a[j] = a.a[j], a.a[i]


def trasnsform3(a: Matrix, i, x):
    for j in range(a.m):
        a.a[i][j] *= x


def gauss(a: Matrix, b: list):
    if a.n != len(b):
        raise Exception

    n = a.n
    m = a.m

    c = Matrix(n, m + 1)

    for i in range(n):
        for j in range(m):
            c.set(i, j, a.get(i, j))

    for i in range(n):
        c.set(i, m, b[i])

    row = 0
    for j in range(m):
        if a.get(row, j) == 0:
            for i in range(row + 1, n):
                if c.get(i, j) != 0:
                    transform2(c, i, row)
                    break

        if c.get(row, j) == 0:
            continue

        for i in range(row + 1, n):
            transform1(c, i, row, -Fraction(c.a[i][j], c.a[row][j]))
        row += 1

    no_solution = False
    for i in range(n):
        flag = True
        for j in range(m):
            if c.get(i, j) != 0:
                flag = False
                break

        if flag and c.get(i, m) != 0:
            no_solution = True
            break

    if no_solution:
        print("No solution")
    else:
        for i in range(n):
            for j in range(m):
                if c.get(i, j) != 0:
                    for row in range(0, i):
                        transform1(c, row, i, -Fraction(c.get(row, j), c.get(i, j)))
                    break

        print(c)