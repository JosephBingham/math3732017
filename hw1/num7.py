import math, time
gc = 32.17
sin = 300
m = 0.25
k = 0.1
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
