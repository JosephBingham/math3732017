# HW4 :: Joey Bingham :: Math 373

## 1.

### a. 
	Note the error formula for the forward and backward differents method is given 
	max over c |(1/12) * (b - a)^3 * f''(c)| c in [a,b]. This yields 1/12*|sin(c)|
	Using forward-differents f'(.5) ~~ (f(.6) - f(.5))/|(.6 - .5)| = (0.5646 - 0.4794)/.1 
	= 0.852, actual = 0.877, error = 0.025, theoretical error = sin(.6)/12 = 0.04705
	Using forward-differents f'(.6) ~~ (f(.7) - f(.6))/|(.7 - .6)| = (0.6442 - 0.5646)/.1 
	= 0.796, actual = 0.825, error = 0.02935, theoretical error = sin(.7)/12 = 0.05368
	Using backwards-differents f'(.7) ~~ (f(.7) - f(.6))/|(.7 - .6)| = (0.6442 - 0.5646)/.1 
	= 0.796, actual = 0.764, error = 0.03115, theoretical error = sin(.7)/12 = 0.05368

### b. 
	
	#!/usr/bin/python
	
	x = 1.0
	
	f = lambda x: x**2
	
	print "N : ESTIMATE : ERROR"
	
	for i in xrange(1, 11):
		h = 10**-i
		est = (f(x + h) - f(x))/h
		err = 2 - est
		print "%d : %8.6f : %f" % (i, est, err)
	
	Which yields,
	N : ESTIMATE : ERROR
	1 : 2.100000 : -0.100000
	2 : 2.010000 : -0.010000
	3 : 2.001000 : -0.001000
	4 : 2.000100 : -0.000100
	5 : 2.000010 : -0.000010
	6 : 2.000001 : -0.000001
	7 : 2.000000 : -0.000000
	8 : 2.000000 : 0.000000
	9 : 2.000000 : -0.000000
	10 : 2.000000 : -0.000000
	Which confirms the limit definition of the derivative 

## 2.

### a.
	By the definition of the trapezoidal rule, this is = (b - a) * (f(b) - f(a))/2
	= (1 - .5) * (1^4 - .5^4)/2 = (1 - .5^4)/4 = 0.234375, actual error = .0405625, 
	theoretical error (b - a)^2 / 12 * ( f'(b) - f'(a) ) = 1/16

### b. 
	By the definition of simpson's rule, this is = (b - a)/6 * (f(a) + 4*f((a + b)/2) +f(b))
	plugging in a and b we get = 0.19401, actual error = 0.000260
	
### c.
	#!/usr/bin/python

	def trap(f, a, b):
		return (f(b) + f(a))/2.0
	
	def comTrap(f, a, b, n):
        	d = (b - a)/((n - 1) * 1.0)
        	p = [a + x*d for x in xrange(n)]
        	i = 0
        	val = []
        	while i < n - 1:
                	val.append(trap(f, p[i], p[i+1]))
                	i += 1
        	return sum(val)*d
	
	f = lambda x: x**4
	
	print comTrap(f, .5, 1, 4)
	
	which gave 0.20183899177, this is an error of 0.00808

### d. 
	#!/usr/bin/python
	
	def comSimpson(f, a, b, n):
        	d = (b - a)/((n - 1) * 1.0)
        	p = [a + x*d for x in xrange(n)]
        	val = f(a)
        	val += 2*sum([f(p[2*j]) for j in xrange(1, n/2)])
        	val += 4*sum([f(p[2*j - 1]) for j in xrange(1, n/2 + 1)])
        	val += f(b)
        	val *= (b - a)/(3*(n + 1))
        	return val
	
	f = lambda x: x**4
	
	print comSimpson(f, .5, 1, 4)
	
	
	which gave 0.227237654321 which had an error of 0.03308
	
### e. 
	see c. and d.

### f.
	see c.


## 3.

### a.
	To show this, we must show that these values can be derived from the following system of 
	equations (all integrals marked ∫ are from -1 to 1):
	∫dx = a + b
	∫xdx = ax + by,
	From these, we get the system 
	[1 1]*[a] = [2]
	[x y] [b]   [0], from this we get that a = b = 1, and from the derivation from Newton-Cotes
	We get that x = -y gets us that x = sqrt(3)/3 = -y.	

### b.
	Shifting the interval, we get that x = .5[(.5)t + 1.25] and dx = .25t using the same transformation
	as the last homework. Thus this is now f(t) = (.078125t^2 + .15625t + .390625)*ln(.25t + 1.25)


#### n = 2
	We get f(-sqrt(3)/3) +  f(sqrt(3)/3) = 0.0327907246065 + 0.168495983479 = 0.201286708086

#### n = 3
	We get .555555*f(-.77459666692) + .555555*f(.77459666692) + .888888*f(0) = 0.201050726259

#### n = 5
	We get .2369268851 * f(-.9061798459) +  .2369268851 * f(.9061798459) + 
	.4786286705*f(-.5384693101)  + .4786286705*f(.5384693101) + .56888888*f(0) =
	0.20104971026

## 4.

### a.
	Note that sin(x) can be expressed as a taylor series sum(0:inf, (-1)^n * x^(2n+1) / (2n + 1)!)
	Thus this integral is actually the integral from 0 to 1 of 
	sum(0:inf, (-1)^n * x^(2n+.75) / (2n + 1)!) which is approximately 0.5284078 using my code
	from the question 2

### b.
	Take t = 1/x, and 1/t = x, this then becomes the integeral from 0 to 1 of cos(t^-1)*t
	This is approximately 0.0181 using my code from question 2

## 5.

### a.
	Starting by scaling the first element and eliminating the first colomn
	1	-0.75	1.5	0.5
	0	-0.75	3.5	3.5
	0	-1.5	-1	-1
	And such we get
	1	-0.75	1.5	0.5
	0	1	-14/3	-14/3 
	0	-1.5	-1	-1

	1	0	-2	-3
	0	1	-14/3	-14/3 
	0	0	-8	-8

	1	0	-2	-3
	0	1	-14/3	-14/3 
	0	0	1	1
	using back substitution, we get that x3 = 1, x2 = -14/3 - (-14/3) = 0, x1 = -2 - (-3) = 1.

### b.
	4	-4.5	5	1
	-1	0	2	3
	2	-1.5	3	1

	1	-1.125	1.25	.25
	0	-1.125	3.25	3.25
	0	1	.5	.5

	1	-1.125	1.25	.25
	0	1	-2.8888	-2.8888
	0	0	3.38888 3.38888
	using back substitiution, we get that x3 = 1, x2 = -2.8888 - (-2.8888) = 0, x1 = 1.25 - .25 = 1


### c.
	


## 6.

### a.
	Consider that this is of the form LUx = b, let Ux = y, if we solve Ly = b, then Ux = y, we
	will have the solutions,
	y1 = 2, y2 = -5, y3 = 4, then
	x1 = 2 + 4/3 - 15/2, x2 = 5/2 - 2/3, x1 = 4/3

### b.
	!/usr/bin/python
	from scipy import *
	
	def lunopiv(A):
    	m,n = shape(A)
    	for i in arange(0,n):
        	pivot = A[i,i]
        	for k in arange(i+1,n):
            	A[k,i] = A[k,i]/pivot
            	A[k,i+1:n] = A[k,i+1:n] - A[k,i]*A[i,i+1:n]
    	L = eye(n)+tril(A,-1)
    	U = triu(A)
    	return L,U
	
	A = array([ [2, 3, -1], [4, 4, -1], [-2, -3, 4] ])
	
	print lunopiv(A)

	Which printed

	(array([[ 1.,  0.,  0.],
		[ 2.,  1.,  0.],
       		[-1.,  0.,  1.]]), 
	 array([[ 2,  3, -1],
		[ 0, -2,  1],
		[ 0,  0,  3]]))
	Which is the same as the matrix in part a of this question.

## 7.

### a.
	#!/usr/bin/python
	import numpy
	def ldl(A):
        	A = numpy.matrix(A)
        	S = numpy.diag(numpy.diag(A))
        	Sinv = numpy.diag(1/numpy.diag(A))
        	D = numpy.matrix(S.dot(S))
        	Lch = numpy.linalg.cholesky(A)
        	L = numpy.matrix(Lch.dot(Sinv))
        	return L, D
	
	A = numpy.matrix([[2., -1., 0.], [-1., 2., -1.], [0., -1., 2.]])
	
	L, D = ldl(A)
	
	print L
	print D
	
	Which gave,
	[[ 0.70710678  0.          0.        ]
	 [-0.35355339  0.61237244  0.        ]
	 [ 0.         -0.40824829  0.57735027]]
	[[ 4.  0.  0.]
	 [ 0.  4.  0.]
	 [ 0.  0.  4.]]
	Which gives us that x1 = 5/4, x2 = 1/2, x3 = 3/4


### b.
	#!/usr/bin/python
	import numpy
	from numpy.linalg import cholesky

	A = numpy.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])

	print cholesky(A)
	
	Which gave:
	[[ 1.41421356  0.          0.        ]
	 [-0.70710678  1.22474487  0.        ]
	 [ 0.         -0.81649658  1.15470054]]
	Which gives us that x1 = 5/4, x2 = 1/2, x3 = 3/4
