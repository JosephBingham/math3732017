# Homework 1: Math 373: Joseph Bingham

## Number 1:
### a)
	Note that 5 - (ln(5)^5) is approximately -5.7986... which is 
	clearly less than 0. Further note that 4 - (ln(4)^4) is 
	approximately .3066... which is clearly greater than 0. 
	Thus, by the intermediate value theorem and the continuity
	of the function we have that there must exist a c in (4, 5) 
	so that c - (ln(c)^c) = 0.

### b)
	- Existance: Note that for any k, we get that limit of x^3 + 2x + k as x 
	goes to infinity will clearly always goes to infinity. Also
	note that the limit of x^3 + 2x + k as x goes to negative infinity will
	clearly go to negative infinity for any finite value k, as 
	this limit is the same as asking the limit as x goes to positive
	infinity for -x^3 - 2x + k.
	- Uniqueness: Consider the fact that the derivative of this 
	function is 3x^2 + 2, which is a strictly positive function 
	which does not depend on k. This means that for any k, the 
	function will always be increasing. For sake of contradiction,
	suppose that there is more than one root, and pick 2 roots, 
	a and b. Without loss of generality say that a < b. By Rolle's
	theorem, there must exist c in (a, b) so that the derivative at
	c is 0, which is not a strictly positive, thus contradiction

## Number 2: 
	The third degree polynomial of f(x) centered at 0 yields 
	P_3(x) = -4 + 6x - x^2 - 7(x^3)/3. This yeilds P_3(.4) = 
	-4 + 6(.4) - (.4)^2 - 7(.4^3)/3 which is aproximately -1.9093...
	To bound the error, consider the formula for the Taylor remainder 
	function for the third degree polynomial, R(x) = 
	(sin(2z) + zcos(2z)/3)x^4, where z is maximizes R and is 
	from [0, .4], and x = .4. Using critical point analysis and 
	the derivate test to find the max of R(z), we get that the 
	error < .09733... The real error is .09330...

## Number 3:
### a) 
	By definition, fhat(x) = f(x + l), so the absolute error is
	equal to |f(x) - f(x + l)|. By the mean value theorem, this 
	is equal to f'(c)|x - (x + l)| = f'(c)|l| for some c in (x, x + l).
	The relative error would thusly be f'(c)|l|/|f(x)|.

### b)
#### i.
	The bound on the absolute error exp(x) would be 
	max{exp(c)|5*10^-6| : c in (1, 1 + 5*10^-6)} which is around
	1.36*10^-5. The relative error would be 1.36*10^-5/exp(1), 
	this is about 5*10^-6.
#### ii.
	The bound on the absolute error sin(x) would be 
	max{sin(c)|5*10^-6| : c in (1, 1 + 5*10^-6)} which is around
	4.3*10^-6. The relative error would be 4.3*10^-6/sin(1), 
	this is about 5*10^-6.
## Number 4:
	All code for this homework was written in python 2.7.14:

	import math, time

	f = lambda x: 4*x**2 - math.e**x - math.e**(-x)
	df = lambda x: 8*x - math.e**x + math.e**(-x)

	def newton(f, df, pin, tol, Maxiters):
        	timer = time.time()
        	iters = 0
        	while iters < Maxiters:
                	iters = iters + 1
                	p = pin - float(f(pin))/df(pin)
                	if abs(p - pin) < tol:
                       		break
               		pin = p
        	return (p, f(p), time.time()-timer)

	for pin in [-10, -5, -3, -1, 0, 1, 3, 5, 10]:
        	try:
               		print pin, newton(f, df, pin, 10**-5, 10**9)
        	except ZeroDivisionError:
                	print "{} caused a zero division error".format(pin)
	

	which gave the following outputs:
	-10 (-4.30624527352012, -3.268496584496461e-13, 0.00011396408081054688)
	-5 (-4.3062452735222365, -8.434142273472389e-11, 2.002716064453125e-05)
	-3 (0.824498585291139, 2.7755575615628914e-16, 1.6927719116210938e-05)
	-1 (-0.8244985852911388, 0.0, 4.291534423828125e-05)
	0 0 caused a zero division error
	1 (0.8244985852911388, -1.6653345369377348e-16, 1.3828277587890625e-05)
	3 (-0.824498585291139, 4.440892098500626e-16, 1.5974044799804688e-05)
	5 (4.3062452735222365, -8.433591498768767e-11, 1.5974044799804688e-05)
	10 (4.30624527352012, -3.2145987260978615e-13, 3.1948089599609375e-05)
	As one can see, the 0 case caused a fatal error. Also, due to
	the nature of the curve we are looking at, values that are close
	will not necissarily go to the same root. For example,
	while p = -5 and -1 both went to negative roots, -3 did not.
	The opposite can be said for 1, 3, and 5. Also, the value 
	does not seem to have much influence on the time taken.

## Number 5:

	import math
	import time
	f = lambda x: 1 - 4*x*math.cos(x) + 2 * x**2 + math.cos(2*x)

	df = lambda x: -4*math.cos(x) - 4*x*math.sin(x) + 4*x - 2*math.sin(2*x)

	ddf = lambda x: -4*math.sin(x) - 4*x*math.cos(x) + 4 - 4*math.cos(2*x)

	def newton(f, df, pin, tol, Maxiters):
        	timer = time.time()
        	iters = 0
        	while iters < Maxiters:
        	        iters = iters + 1
        	        p = pin - float(f(pin))/df(pin)
        	        if abs(p - pin) < tol:
        	                break
        	        pin = p
        	return (p, f(p), time.time()-timer)


	def mod_newton(f, df, ddf, pin, tol, Maxiters):
        	timer = time.time()
        	iters = 0
        	while iters < Maxiters:
        	        iters = iters + 1
        	        p = pin - (df(pin)*f(pin))/(df(pin)**2-f(pin)*ddf(pin))
        	        if abs(p - pin) < tol:
        	                break
        	        pin = p
        	return (p, f(p), time.time()-timer)

	print newton(f, df, .5, 10**-10, 10**10)
	print mod_newton(f, df, ddf, .5, 10**-10, 10**10)

	This yielded:
	(0.7390767013940737, 3.9827302567019274e-10, 0.29070210456848145)
	(0.7390767013822329, 3.982740526264905e-10, 0.6488118171691895)
	This goes to show that the newton's method is quicker, but less accurate.

## Number 6:
	
	Code:
	#!/usr/bin/python
	import time, math

	f = lambda x: 600*x**4 - 500*x**3 + 200*x**2 - 20*x - 1
	df = lambda x: 2400*x**3 - 1500*x**2 + 400*x - 20

	def bisection(f, a, b, tol, maxiters):
		timer = time.time()
		iters = 0
		p = (a + b)/2.0
		while iters < maxiters:
			iters = iters + 1
			if f(a) * f(p) < 0:
				b = p
			elif f(b) * f(p) < 0:
				a = p
			p = (a + b)/2.0
			if abs(a - p) < tol and abs(f(p))< tol:
				break
		return (p, f(p), iters, time.time() - timer)

	def newton(f, df, pin, tol, maxiters):
		timer = time.time()
		iters = 0
		while iters < maxiters:
			iters = iters + 1
			p = pin - f(pin)/df(pin)
			if abs(p - pin) < tol:
				break
			pin = p
		return (p, f(p), iters, time.time()-timer)

	def secant(f, a, b, tol, maxiters):
		timer = time.time()
		iters = 0
		while iters < maxiters:
			iters = iters + 1
			p = a - f(a)*((b - a)/(f(b) - f(a)))
			if abs(a - p) < tol or abs(f(p)) < tol:
				break
			if f(a) - f(b) > 0:
				a = p
			else:
				b = p
		return (p, f(p), iters, time.time()-timer)


	def muller(f, p0, p1, p2, tol, maxiters):
		timer = time.time()
		iters = 0
		while iters < maxiters:
			iters = iters + 1
			h1 = p1-p0
    			h2 = p2-p1
    			delta1 = (f(p1)-f(p0))/h1
    			delta2 = (f(p2)-f(p1))/h2
    			d = (delta2-delta1)/(h2+h1)
    			b = delta2+h2*d
		        D = math.sqrt(b**2-4*f(p2)*d)
    			if abs(b-D) < abs(b+D):
			        E = b+D
    			else:
        			E = b-D
		        h = -2*f(p2)/E
    			p = p2+h
    			if abs(h)<tol:
        			break
    			p0= p1
    			p1= p2
    			p2= p
		return (p, f(p), iters, time.time()-timer)


	print bisection(f, 0, 1, 10**-4, 10**9)
	print newton(f, df, .5, 10**-4, 10**9)
	print secant(f, 0.1, .5, 10**-4, 10**9)
	print muller(f, .1, .3, .5, 10**-4, 10**9)


	Which yielded:
	(0.2020721435546875, -2.60843625090601e-05, 15, 9.894371032714844e-05)
	(0.20207350231204924, 2.51306377485605e-07, 5, 2.2172927856445312e-05)
	(0.20206866187849537, -9.356606961219427e-05, 11, 0.00010395050048828125)
	(0.20207348935162037, 1.0435119435214801e-10, 5, 6.103515625e-05)
	As expected, Newtons's method did the best, as it was using 
	the most information about the function to get to the root 
	the quickest. Secant method, using the least, did the 
	worst, not even getting to the root under 1*10^-4 seconds. 
	What was suprising, though was the fact that Muller's method
	was the most accurate of them all. I thought that Newton's 
	would be. I think this is due to the quadratic nature of
	the graph of f that it lends itself to being aproximated well
	by Muller's method. 

## Number 7:
	Code:
	import math, time
	gc = 32.17
	sin = 300
	m = 0.25
	k = 0.1
	def s(t):
	s = lambda t: sin - t*m*gc/k + (t**2)*(m**2)*gc/(k**2)*(1 - math.e**(-t*(k)/m))
	ds= lambda t: -m*gc/k + 2*t*(m**2)*gc/(k**2)*(1 - math.e**(-t*(k)/m)) + (t**2)*((m**2)*gc/k**2)*((k/m)*math.e**(-t*(k)/m))
	g = lambda t: (sin + (m**2)*gc/(k**2) * (1 - (math.e)**(-t*(k)/m)) * (k/(m*gc)))


	def newton(f, df, pin, tol, maxiters):
		timer = time.time()
		iters = 0
		while iters < maxiters:
			iters = iters + 1
			p = pin - f(pin)/df(pin)
			if abs(p - pin) < tol:
				break
			pin = p
		return (p, f(p), iters, time.time()-timer)

	def steff(f, pin, tol, maxiters):
		timer = time.time()
		iter = 0
		while iter < maxiters:
			iter = iter + 1
			p1 = f(pin)
			p2 = f(p1)
			p = pin - (p1-pin)**2/(p2-2*p1+pin)
			if abs(pin - p) < tol:
				break
			pin = p
		return (p, f(p), iter, time.time()-timer)

	def fixed_point(g, pin, tol, maxiters):
		timer = time.time()
		iter = 0
		while iter < maxiters:
			iter = iter + 1
			p = g(pin)
			if abs(p-pin)<tol:
				break
			pin = p
		return (p, g(p), iter, time.time()-timer)

	print newton(s, ds, 5, .01, 10**9)
	print fixed_point(g, 5, .01, 10**9)
	print steff(s, 5, .01, 10**9)
	Which yielded: 
	(-1.5618555006623365, -0.0004958176173204265, 34, 0.0002980232238769531)
	(302.5, 302.5, 3, 1.0967254638671875e-05)
	(4.995037654952678, 4234.593543590172, 1, 1.71661376953125e-05)
	I suspect these results are due to the odd nature of the function s.





