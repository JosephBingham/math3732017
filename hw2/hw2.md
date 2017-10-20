# HW2 :: Joey Bingham :: Math 373

## 1.
### a.
	All code for this assignment will be done in python
	version 2.7.14

	#!/usr/bin/python

	xs = [0.0 ,.25 ,.5 , .75]
	fxs = [1.0, 1.64872, 2.71828, 4.48169]
	x = .43

	def main():
		for i in xrange(3):
			degree = i+1
			print "degree ", degree
			p = 0
			for j in xrange(degree):
				p += fxs[j]*L(degree, j)
			print p

	def L(n, k):
		i = 1
		for l in xrange(n):
			if not l == k:
				i *= (x - xs[l])/(xs[k] - xs[l])
		return i

	if __name__ == '__main__':
		main()
	
	this yeilded:
	degree  1
	1.0
	degree  2
	2.1157984
	degree  3
	2.376382528
### b.
	#!/usr/bin/python
	import numpy as np

	def main():
	        xi = [0., .25, .5, .75]
	        fi = [1, 1.64872, 2.71828, 4.48169]
	        x = .43
	        q = neville(x, xi, fi)
	        print q

	def neville(x, xi, fi):
	        n = len(xi) - 1
	        m = np.zeros((n+1, n+1))
	        for i in xrange(len(fi)):
	                m[i][0] = fi[i]
	        for i in xrange(n):
	                for j in xrange(i+1):
	                        if not xi[i+1]-xi[i-(j+1)] == 0:
	                                m[i+1][j+1] = ((x-xi[i-(j+1)])*m[i+1][j]-(x-xi[i+1])*m[i][j])/(xi[i+1]-xi[i-(j+1)])
	                        else: #this is an artifact of pythons odd indexing rules.
	                                m[i+1][j+1] = ((x-xi[i-(j)])*m[i+1][j]-(x-xi[i+1])*m[i][j])/(xi[i+1]-xi[i-(j)])

		return m

	if __name__ == '__main__':
	        main()

	which yeilds:
	[[ 1.          0.          0.          0.        ]
	 [ 1.64872     1.4151808   0.          0.        ]
	 [ 2.71828     2.5685416   2.89148262  0.        ]
	 [ 4.48169     3.3531076   3.01835944  2.96422533]]



### c.
	The bound on the error for n = 1 can be found by 
	max of l in [0, .5] |f''(x)(x-0)(x-.25)| = 
	1.3631606937057947
	and the actual error was 
	1.3591409142295225
	The bound on the error for n = 2 can be found by 
	max of l in [0, .75] |f'''(x)(x-0)(x-.25)(x-.5)| = 
	0.8403167006883872
	actual error was
	0.24736229370579466
### d. 
	import numpy as np

	def d(x, f):
	        n = len(x) -1
	        F = np.zeros((n+1, n+1))
	        for i in xrange(len(f)):
	                F[i][0] = f[i]

	        for i in xrange(n):
	                for j in xrange(i+1):
	                        if not x[i+1] - x[i-(j+1)] == 0:
	                                F[i+1][j+1] = (F[i+1][j]-F[i][j])/(x[i+1]-x[i-(j+1)])
	                        else:
	                                F[i+1][j+1] = (F[i+1][j]-F[i][j])/(x[i+1]-x[i-j+1])
	        return F

	x = [0., .25, .5, .75]
	f = [1, 1.64872, 2.71828, 4.48169]
	print d(x, f)

	which yeilded 
	[[  1.           0.           0.           0.        ]
	[  1.64872     -1.29744      0.           0.        ]
	[  2.71828      2.13912    -13.74624      0.        ]
	[  4.48169      3.52682      1.85026667  31.19301333]]

## 2.
### a. 
#### i.
	Decomposing the sum, we get 0 -> 0, 1 -> 3*(1/3)x(1-x)^2 -> x-2x+x^3, 2 -> (3!/2!)*(2/3)x^2(1-x) -> 2x^2 - 2x^3, 3 -> x^3
	thus giving us x.
#### ii.
	Again, decomposing the sum, we get 0 -> 1-3x+3x^2-x^3, 1 -> 3x-6x^2+3x^3, 2 -> 3x^2-3x^3, 3 -> x^3 which gives us 1.
### b.
	Consider that c(n-1, k-1) = (n-1)!/(k-1)!((n-1)-(k-1))! = (n-1)!/(k-1)!(n-k)! = (k/n)(n-1)!*n/k*(k-1)!(n-k)! = (k/n)n!/k!(n-k)! =
	(k/n)c(n,k).  
### c. 
	Note that c(n, k) = (n(n-1)/k(k-1)) c(n-2, k-2) by similar logic to above. Now consider that n^2*Bn(x) = sum(k=0:n, c(n, k) (k^2) (x^k) (1-x)^(n-k)
	= sum(k=0:n, c(n, k)k(k-1)x^k(1-x)^(n-k)+sum(k=1:n, c(n, k) kx^k (1-x)^(n-k))
	= sum(k=2:n, n(n-1)c(n-2, k-2) x^2 x^(k-2) (1-x)^((n-2)-(k-2)) + sum(k=1:n, n c(n-1, k-1) x x^(k-1) (1-x)^((n-1)-(k-1)))
	= n(n-1) x^2 sum(k=0:n-2, c(n-2, k) x^2 (1-x)^((n-2)-k) + nx sum(k=0:n-1, c(n-1, k) x^k (1-x)^((n-1)-k))
	= n(n-1) x^2 + n x
	n^2Bn(x) = n(n-1) x^2 + n x -> Bn(x) = (n-1)/n x^2 + x/n
### d. 
	E = |((n-1)/n)*x^2 + x/n - x^2| -> |x^2((n-1)/n - n/n) + x/n| -> |(x-x^2)/n| which implies that to find the n, we maximize the top.
	The max value of the top is x = .5 which yeilds .25, so the smallest n to give us E < 10e-6 is n=10e6*.25.
	
## 3.
### a. 
	P(x) was interpolated using lagrange's method while Q(x) was interpolated using newton's method
### b. 
	This does not violate uniqueness because they are both equal to 1-3x+x^3, and are thus the same.

## 4. 
### a and b

	import math

	#degree 3, found by using rrech of varible matrix 
	f = lambda x: 3*x*math.e**x - math.e**(2*x)
	cooef = [1.440418999990135, -7.624829999971098, 11.694199999971794 ,-4.743999999990829]
	ansd3 =0
	for c in xrange(len(cooef)):
	        ansd3 += (1.03)**c * cooef[c]
	print "degree 3: ", ansd3
	print f(1.03)
	print "error : ", ansd3 - f(1.03)

	#degree 5, found by using rrech of varible matrix
	cooef =[-1.274338856423367, 2.472088954744194, -1.8224693372779122, 2.3672481600678665, 0.4863798451622997, -0.49036107594861567]
	ansd5 = 0
	for c in xrange(len(cooef)):
	        ansd5 += (1.03)**c * cooef[c]
	print "degree 3: ", ansd5
	print f(1.03)
	print "error : ", ansd5 - f(1.03)

	which gave:
	degree 3:  0.809323992
	0.809323618902
	error :  3.73098294482e-07
	degree 3:  0.809323729456
	0.809323618902
	error :  1.09484932669e-08

## 5.
### a and b.
	#!/usr/bin/python
	from scipy.interpolate import CubicSpline
	x = [0, 1, 2]
	y = [0, 1, 2]
	print CubicSpline(x,y).c
	print CubicSpline(x,y,bc_type = 'clamped').c

	Gave the coefficents:
	[[ 0.  0.]
	 [ 0.  0.]
	 [ 1.  1.]
	 [ 0.  1.]]
	[[-0.5 -0.5]
	 [ 1.5  0. ]
	 [ 0.   1.5]
	 [ 0.   1. ]]
