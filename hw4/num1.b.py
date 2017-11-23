#!/usr/bin/python

x = 1.0

f = lambda x: x**2

print "N : ESTIMATE : ERROR"

for i in xrange(1, 11):
	h = 10**-i
	est = (f(x + h) - f(x))/h
	err = 2 - est
	print "%d : %8.6f : %f" % (i, est, err)
