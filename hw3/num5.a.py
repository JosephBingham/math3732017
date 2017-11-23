	####5a
	#!/usr/bin/python
	from numpy import *
	from matplotlib.pyplot import *
	from scipy.integrate import quad
	import math
	#from numpy.fft import fft
	#from numpy.polynomial.legendre import legval
	n = 3
	
	a = zeros(n)
	b = zeros(n)
	f = lambda x: math.e**x
	f_a = lambda x,k: math.cos(k*x)*(math.e**x)
	f_b = lambda x,k: math.sin(k*x)*(math.e**x)
	for k in xrange(n):
		a[k], _ = quad(f_a, -math.pi, math.pi, k)
		b[k], _ = quad(f_b, -math.pi, math.pi, k)
		a[k] /= math.pi
		b[k] /= math.pi
	a = array(a)
	b = array(b)
	a0, _ = quad(f, -math.pi, math.pi)
	a0 /= math.pi
	
	x = array(linspace(-math.pi, math.pi, 1000))
	k = array(xrange(1,1001))
	
	x_k = x.dot(k)
	
	s = a0/2 + math.cos(x_k)*a + sin(x_k)*b
	
	fig, ax = subplots()
	ax.plot(s, '-o', ms=20, lw=2, alpha=.7, mfc='orange')
	ax.grid()
	
	fig.text(.9, .05, '5a', fontsize=50, color='gray', ha='right', va='bottom', alpha=.5)
	
	show()
	
	
	####5b
	
	#!/usr/bin/python
	from numpy import *
	from matplotlib.pyplot import *
	from scipy.integrate import quad
	import math
	#from numpy.fft import fft
	#from numpy.polynomial.legendre import legval
	n = 3
	m = 6
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
	
	####5c
	#!/usr/bin/python
	from numpy import *
	from matplotlib.pyplot import *
	from scipy.integrate import quad
	import math
	#from numpy.fft import fft
	#from numpy.polynomial.legendre import legval
	n = 8
	m = 8
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
	
