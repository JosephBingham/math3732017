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

f = lambda x: x**.75 - (x**2.75)/6 + (x**4.75)/120 - (x**6.75)/5040


print comSimpson(f, 0, 1, 4)
