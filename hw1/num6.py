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
