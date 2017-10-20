#!/usr/bin/python
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
