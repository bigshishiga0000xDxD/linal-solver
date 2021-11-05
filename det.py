from matrix import *
import gauss


def det(a: Matrix) -> Fraction:
    if a.n != a.m:
        raise Exception

    c, _, multiplier = gauss.runGauss(gauss.appendMatrix(a, Matrix(a.n, 0)), a.n, a.m)

    if c.get(a.n - 1, a.m - 1) == 0:
        return Fraction(0)
    else:
        return Fraction(1, multiplier)
