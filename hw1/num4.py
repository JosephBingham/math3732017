#!/usr/bin/python
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
