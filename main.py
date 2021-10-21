from fractions import Fraction

from matrix import *
from gauss import *


def task(n):
    print('task: {}'.format(n))


task(2)

A = Matrix([
    [1, 2, -3, -1, 9, 0],
    [-9, 0, 10, 0, 0, 9],
    [0, 0, 0, 3, -8, -3]
])

B = Matrix([
    [0],
    [0],
    [0]
])

gauss(A, B)

task(3)

A = Matrix([
    [33, 0, -1, 0],
    [-10, -9, 2, -1],
    [-2, -5, 1, 2]
])

B = Matrix([
    [37, 1, 103],
    [9, -8, -57],
    [9, -12, -18]
])

gauss(A, B)

task(4)

A = Matrix([
    [20, -3, -5, 35, -30],
    [12, -1, -4, 20, -16],
    [5, -1, -1, 9, -8],
    [-7, 1, 2, -12, 10]
])

gauss(A, E(4), force_print=True)

task(5)

A = Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [3, 2, 7]
])

B = Matrix([
    [1, 0, 3, -6],
    [0, 1, -7, 7],
    [2, 2, -8, 2]
])

C = Matrix([
    [1, 0, -2, 1],
    [1, 1, -4, -1],
    [-1, -2, 7, 4],
    [2, 2, -6, 1]
])

D = Matrix([
    [-4, 16, 5, 0],
    [4, 9, 0, 10],
    [-16, -11, 5, -30],
    [8, 43, 5, 30]
])

U = A * B * inv(C)
gauss(U)
gauss(D)
