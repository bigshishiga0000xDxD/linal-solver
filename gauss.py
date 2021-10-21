from matrix import *


def transform1(a: Matrix, i, j, x):
    if i == j:
        raise Exception

    for k in range(a.m):
        a.a[i][k] += a.a[j][k] * x


def transform2(a: Matrix, i, j):
    a.a[i], a.a[j] = a.a[j], a.a[i]


def transform3(a: Matrix, i, x):
    if x == 0:
        raise Exception

    for j in range(a.m):
        a.a[i][j] *= x


def appendMatrix(a: Matrix, b: Matrix):
    c = Matrix(a.n, a.m + b.m)

    for i in range(a.n):
        for j in range(a.m):
            c.set(i, j, a.get(i, j))

    for i in range(b.n):
        for j in range(b.m):
            c.set(i, a.m + j, b.get(i, j))

    if b.m != 0:
        c.setLine(a.m - 1)
    return c


def splitMatrix(c: Matrix):
    if c.line is None:
        raise Exception

    a = Matrix(c.n, c.line + 1)
    b = Matrix(c.n, c.m - a.m)

    for i in range(a.n):
        for j in range(a.m):
            a.set(i, j, c.get(i, j))

    for i in range(b.n):
        for j in range(b.m):
            b.set(i, j, c.get(i, a.m + j))

    return a, b


def runGauss(c: Matrix, n: int, m: int):
    row = 0
    for j in range(m):
        if row == n:
            break

        if c.get(row, j) == 0:
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

        if flag:
            for j in range(m, c.m):
                if c.get(i, j) != 0:
                    no_solution = True
                    break

            if no_solution:
                break

    for i in range(n):
        for j in range(m):
            if c.get(i, j) != 0:
                for row in range(0, i):
                    transform1(c, row, i, -Fraction(c.get(row, j), c.get(i, j)))
                transform3(c, i, Fraction(1, c.get(i, j)))
                break

    return c, no_solution


def gauss(a: Matrix, b=None, force_print=False):
    if b is None:
        b = Matrix(a.n, 0)
    elif a.n != b.n:
        raise Exception

    c, no_solution = runGauss(appendMatrix(a, b), a.n, a.m)

    if no_solution and not force_print:
        print("No solution")
    else:
        print(c)


def inv(a: Matrix):
    if a.n != a.m:
        raise Exception

    c, no_solution = runGauss(appendMatrix(a, E(a.n)), a.n, a.m)

    if no_solution:
        return None
    else:
        a, b = splitMatrix(c)
        return b
