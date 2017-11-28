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
