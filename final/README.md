# Final Project :: math 373 :: Joey Bingham

## 1.

### a. 
	#!/usr/bin/pthon
	#solve odt dy/dt = f(y,t), [tmin, tmax]
	#ivp: y(tmin) = y_0
	
	tmin = 0
	tmax = 1
	y0 = 1
	
	f = lambda t,y: sin(y)
	
	n = 20
	h = (tmax - tmin)/n
	t = [tmin + x*h for x in xrange(n+1)]
	u = [0] * n
	u[0] = y0
	#forward difference
	for k in xrange(n):
		u(k+1) = u(k) + h*f(t[k], u[k])

	PLOT	
### b. 
	#!/usr/bin/pthon
	#solve odt dy/dt = f(y,t), [tmin, tmax]
	#ivp: y(tmin) = y_0
	
	tmin = 0
	tmax = 1
	y0 = 1
	
	f = lambda t,y: sin(y)
	
	n = 20
	h = (tmax - tmin)/n
	t = [tmin + x*h for x in xrange(n+1)]
	u = [0] * n
	u[0] = y0
	#backward difference
	tol = 10**-6
	MaxIter = 100
	for k in xrange(n)
		#fixed point iter
		p0 = u[k] + h*f(t[k], u[u])
		iters = 0
		p = 0
		while iter < MaxIter:
			iters += 1
			p = u[k] + h*f(t[k+1], p0)
			if abs(p - po) < tol:
				break
			p0 = p

		u[k+1] = p
			
	PLOT	

### c. 
	
	#!/usr/bin/pthon

	#Trapzoidal rule	
	tmin = 0
	tmax = 1
	y0 = 1
	
	f = lambda t,y: sin(y)
	
	n = 20
	h = (tmax - tmin)/n
	t = [tmin + x*h for x in xrange(n+1)]
	u = [0] * n
	u[0] = y0
	tol = 10**-6
	MaxIter = 100
	for k in xrange(n)
		#fixed point iter
		p0 = u[k] + h*f(t[k], u[u])
		iters = 0
		p = 0
		while iter < MaxIter:
			iters += 1
			p = u[k] + h/2*f(t[k+1], p0) + f(t[k], u[k])
			if abs(p - po) < tol:
				break
			p0 = p

		u[k+1] = p
			
	PLOT	

## 2.
### a.
	find eigenvalues look at PowerIteration.m for max
				use InverseIteration.m for min

### b.
	#!/usr/bin/python
	import math
	#solve -u''(x) = f(x), [xmin, xmax]
	
	xmin = 0
	xmax = 1
	alpha = 0
	beta = sin(2)
	
	n = 20	
	h = (xmax - xmin)/2.
	u = [0] * (n+1)
	u[0] = alpha
	u[-1] = beta
	f = lambda x: 4*math.sin(2*x)
	A =[[],[]]
	for i in xrange(n-1):
		A[i][i] = 2
		if i:
			A[i][i-1] = -1
		if not i == n-2:
			A[i-1][i] = -1
	rhs = map(f, x[1:])
	rhs *= .5 
	rhs[0] += alpha
	rhs[-1] += beta

	uu, U = Gausse(A, rhs)
	u[1:-2] = uu

	PLOT
