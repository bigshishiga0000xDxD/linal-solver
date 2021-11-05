from matrix import *


class Transformer:
    def __init__(self, a: Matrix):
        self.a = a
        self.multiplier = Fraction(1)

    def transform1(self, i, j, x):
        if i == j:
            raise Exception

        for k in range(self.a.m):
            self.a.a[i][k] += self.a.a[j][k] * x

    def transform2(self, i, j):
        self.a.a[i], self.a.a[j] = self.a.a[j], self.a.a[i]
        self.multiplier *= -1

    def transform3(self, i, x):
        if x == 0:
            raise Exception

        for j in range(self.a.m):
            self.a.a[i][j] *= x

        self.multiplier *= x
