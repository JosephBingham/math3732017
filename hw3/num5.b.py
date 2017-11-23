#!/usr/bin/python
from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import quad
import math
#from numpy.fft import fft
#from numpy.polynomial.legendre import legval
n = 5
m = 10
a = zeros(n)
b = zeros(n)
x = []
for i in xrange(2*m -1):
	x.append(-math.pi + i/(m*math.pi))
f = lambda x: math.e**x
x = array(x)
y = array([f(i) for i in x])
a = array(a)
b = array(b)
for k in xrange(n):
	tempx_a = array([math.cos(k*j) for j in x])
	tempx_b = array([math.sin(k*j) for j in x])
	a_k = y.dot(tempx_a)/m
	b_k = y.dot(tempx_b)/m
	a[k] = a_k
	b[k] = b_k

a0 = sum(y)/m

x = array(linspace(-math.pi, math.pi, 1000))
k = array(xrange(1,1001))

x_k = x.dot(k)

s = abs(a0/2 + math.cos(x_k)*a + sin(x_k)*b)

fig, ax = subplots()
ax.plot(s, '-o', ms=20, lw=2, alpha=.7, mfc='orange')
ax.grid()

fig.text(.9, .05, '5b', fontsize=50, color='gray', ha='right', va='bottom', alpha=.5)

show()
