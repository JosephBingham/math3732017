# HW4 :: Joey Bingham :: Math 373

## 1.

### a. 
	Using forward-differents f'(.5) ~~ (f(.6) - f(.5))/|(.6 - .5)| = (0.5646 - 0.4794)/.1 = 0.852, actual = 0.877, error = 0.025
	Using forward-differents f'(.6) ~~ (f(.7) - f(.6))/|(.7 - .6)| = ( - 0.5646)/.1 = , actual = , error =
	Using backwards-differents f'(.7) ~~ (f(.7) - f(.6))/|(.7 - .6)| = ( - 0.5646)/.1 = , actual = , error =

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