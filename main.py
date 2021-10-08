from fractions import Fraction

from matrix import *
from gauss import *

A = Matrix([
    [4, -5, 18, -8],
    [5, -8, 26, -10],
    [-4, 4, -16, 8],
    [2, 6, -8, -4]
])

b = [-8, 6, -6, -2]

gauss(A, b)

b = [5, 8, -4, -6]

gauss(A, b)