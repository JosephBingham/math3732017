#!/usr/bin/pthon
#solve odt dy/dt = f(y,t), [tmin, tmax]
#ivp: y(tmin) = y_0
from math import sin
import matplotlib.pyplot as plt

tmin = 0
tmax = 1
y0 = 1

f = lambda t,y: sin(y)

n = 20
h = (tmax - tmin)/float(n)
t = [tmin + x*h for x in xrange(n + 1)]
u = [0] * (n + 1)
u[0] = y0
#forward difference
for k in xrange(n):
        u[k+1] = u[k] + h*f(t[k], u[k])


plt.plot(t, u, 'ro')
plt.show()
