from fractions import Fraction

from matrix import *
from gauss import *
from det import *

A = Matrix([
    [0, 1, -1, -1],
    [7, 1, 4, 1],
    [-2, 2, -4, -3],
    [-8, 0, -5, -2]
])

print(inv(A))
