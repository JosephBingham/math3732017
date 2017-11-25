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
	= (1 - .5) * (1^4 - .5^4)/2 = (1 - .5^4)/4 = 0.234375
	
