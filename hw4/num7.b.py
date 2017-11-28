#!/usr/bin/python
import numpy
from numpy.linalg import cholesky

A = numpy.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])

print cholesky(A)

