#!/usr/bin/python
from math import sin
import matplotlib.pyplot as plt

#Trapzoidal rule
tmin = 0
tmax = 1
y0 = 1

f = lambda t,y: sin(y)

n = 40
h = (tmax - tmin)/float(n)
t = [tmin + x*h for x in xrange(n+1)]
u = [0] * (n + 1)
u[0] = y0
tol = 10**-6
MaxIter = 100
for k in xrange(n):
        #fixed point iter
        p0 = u[k] + h*f(t[k], u[k])
        iters = 0
        p = 0
        while iters < MaxIter:
                iters += 1
                p = u[k] + h/2*(f(t[k+1], p0) + f(t[k], u[k]))
                if abs(p - p0) < tol:
                        break
                p0 = p

        u[k+1] = p
plt.plot(t, u, 'ro')
plt.savefig('num1.c.{}.png'.format(n))

