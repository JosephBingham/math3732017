# Final Project :: math 373 :: Joey Bingham

## 1.

### a. 
	#!/usr/bin/python
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
	
### b. 
	#!/usr/bin/python
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
	t = [tmin + x*h for x in xrange(n+1)]
	u = [0] * (n+1)
	u[0] = y0
	#backward difference
	tol = 10**-6
	MaxIter = 100
	for k in xrange(n):
        	#fixed point iter
        	p0 = u[k] + h*f(t[k], u[k])
        	iters = 0
        	p = 0
        	while iters < MaxIter:
                	iters += 1
                	p = u[k] + h*f(t[k+1], p0)
                	if abs(p - p0) < tol:
                        	break
                	p0 = p
        	u[k+1] = p
	
	plt.plot(t, u, 'ro')
	plt.show()
	
	
### c. 
	
	#!/usr/bin/python
	from math import sin
	import matplotlib.pyplot as plt
	
	#Trapzoidal rule
	tmin = 0
	tmax = 1
	y0 = 1
	
	f = lambda t,y: sin(y)
	
	n = 20
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
	plt.show()
	
	
## 2.
### a.
	Using power iteration method to find the minimum eigenvalue:
	#!/usr/bin/python
	import random
	import numpy as np
	
	def inverseIteration(A, maxIter):
        	m = len(A)
        	n = len(A[0])
        	if not n == m:
                	print 'input is not square'
                	return
        	q = np.random.rand(m)
        	q /= np.linalg.norm(q)
        	lam = 0
        	for i in xrange(maxIter):
                	w = np.dot(A, q)
                	q = w/np.linalg.norm(w)
                	l1 = np.dot(q.T, A)
                	lam = np.dot(l1, q)
        	return lam, q
	
	n = 20
	A = 2*np.eye(n)
	A -= np.eye(n, k = 1)
	A -= np.eye(n, k = -1)
	print inverseIteration(A, 10000)[0]
		
	Which gave
	n = 20
	3.97766165245
	n = 40
	3.99413160237
		
	Using inverse iteration method to find the minimum eigenvalue:
	#!/usr/bin/python
	import random
	import numpy as np
	
	def inverseIteration(A, mu, maxIter):
        	m = len(A)
        	n = len(A[0])
        	if not n == m:
                	print 'input is not square'
                	return
        	q = np.random.rand(m)
        	q /= np.linalg.norm(q)
        	lam = 0
        	w = None
        	for i in xrange(maxIter):
                	inter = A-mu*np.eye(m)
                	w = np.linalg.solve(inter, q)
                	q = w/np.linalg.norm(w)
                	l1 = np.dot(q.T, A)
                	lam = np.dot(l1, q)
        	return lam, q
	
	n = 40
	A = 2*np.eye(n)
	A -= np.eye(n, k = 1)
	A -= np.eye(n, k = -1)
	print inverseIteration(A, 0, 10000)[0]

	which gave
	n = 20
	0.0223383475497
	n = 40
	0.00586839763252 
### b.
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
	
