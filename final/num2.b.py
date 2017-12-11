#!/usr/bin/python
from math import sin
import numpy as np
import matplotlib.pyplot as plt
#solve -u''(x) = f(x), [xmin, xmax]

def gauss(A):
    n = len(A)

    for i in range(0, n):
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x

n = 20
xmin = 0
xmax = 1
alpha = 0
beta = sin(2)

x = np.linspace(float(xmin), float(xmax), n)
n = 20
h = (xmax - xmin)/2.
u = [0] * (n+1)
u[0] = alpha
u[-1] = beta
f = lambda x: 4*sin(2*x)
A = 2*np.eye(n) - np.eye(n, k = 1) - np.eye(n, k = -1)
rhs = map(f, x)
rhs = map(lambda x: .5*x, rhs)
rhs[0] += alpha
rhs[-1] += beta
An = np.c_[A,rhs]
uu = gauss(An)


plt.plot(x, uu, 'ro')
plt.show()
