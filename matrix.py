from fractions import Fraction


class Matrix:
    def __init__(self, *args):
        self.line = None
        if len(args) == 1:
            self.n = len(args[0])
            self.m = len(args[0][0])

            self.a = [[Fraction(0) for _ in range(self.m)] for _ in range(self.n)]

            for i in range(self.n):
                for j in range(self.m):
                    self.a[i][j] = Fraction(args[0][i][j])
        else:
            self.n = args[0]
            self.m = args[1]

            self.a = [[Fraction(0) for _ in range(self.m)] for _ in range(self.n)]

    def __repr__(self):
        result = ""
        max_len = [0] * self.m

        for j in range(self.m):
            for i in range(self.n):
                max_len[j] = max(max_len[j], len(str(self.get(i, j))))

        for i in range(self.n):
            for j in range(self.m):
                s = str(self.get(i, j))
                result += s
                result += ' ' * (max_len[j] - len(s))

                if j == self.line:
                    result += '|'
                result += ' '
            result += '\n'

        return result

    def get(self, i, j):
        return self.a[i][j]

    def set(self, i, j, x):
        self.a[i][j] = Fraction(x)

    def setLine(self, i):
        if i < 0 or i > self.m - 2:
            raise Exception
        self.line = i

    def __neg__(self):
        result = Matrix(self.n, self.m)

        for i in range(self.n):
            for j in range(self.m):
                result.a[i][j] = -self.a[i][j]
        return result

    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            raise Exception

        result = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                result.a[i][j] = self.a[i][j] + other.a[i][j]
        return result

    def __sub__(self, other):
        if self.n != other.n or self.m != other.m:
            raise Exception

        result = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                result.a[i][j] = self.a[i][j] - other.a[i][j]
        return result

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.m != other.n:
                raise Exception

            result = Matrix(self.n, other.m)
            for i in range(self.n):
                for j in range(other.m):
                    for k in range(self.m):
                        result.a[i][j] += self.a[i][k] * other.a[k][j]

            return result
        else:
            result = Matrix(self.n, self.m)
            for i in range(self.n):
                for j in range(self.m):
                    result.a[i][j] = self.a[i][j] * other
            return result

    __rmul__ = __mul__


def T(a: Matrix):
    result = Matrix(a.m, a.n)

    for i in range(a.n):
        for j in range(a.m):
            result.a[j][i] = a.a[i][j]

    return result


def tr(a: Matrix):
    if a.n != a.m:
        raise Exception

    result = Fraction(0)
    for i in range(a.n):
        result += a.a[i][i]

    return result


def E(n: int):
    res = Matrix(n, n)

    for i in range(n):
        res.set(i, i, 1)

    return res
