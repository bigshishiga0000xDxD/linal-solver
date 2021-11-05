from matrix import *
import transformer

def appendMatrix(a: Matrix, b: Matrix) -> Matrix:
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


def splitMatrix(c: Matrix) -> (Matrix, Matrix):
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


def runGauss(c: Matrix, n: int, m: int) -> (Matrix, bool, Fraction):
    t = transformer.Transformer(c)

    row = 0
    for j in range(m):
        if row == n:
            break

        if c.get(row, j) == 0:
            for i in range(row + 1, n):
                if c.get(i, j) != 0:
                    t.transform2(i, row)
                    break

        if c.get(row, j) == 0:
            continue

        for i in range(row + 1, n):
            t.transform1(i, row, -Fraction(c.a[i][j], c.a[row][j]))
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
                    t.transform1(row, i, -Fraction(c.get(row, j), c.get(i, j)))
                t.transform3(i, Fraction(1, c.get(i, j)))
                break

    return c, no_solution, t.multiplier


def gauss(a: Matrix, b=None, force_print=False) -> None:
    if b is None:
        b = Matrix(a.n, 0)
    elif a.n != b.n:
        raise Exception

    c, no_solution, _ = runGauss(appendMatrix(a, b), a.n, a.m)

    if no_solution and not force_print:
        print("No solution")
    else:
        print(c)


def inv(a: Matrix):
    if a.n != a.m:
        raise Exception

    c, no_solution, _ = runGauss(appendMatrix(a, E(a.n)), a.n, a.m)

    if no_solution:
        return None
    else:
        a, b = splitMatrix(c)
        return b
