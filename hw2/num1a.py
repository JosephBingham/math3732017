#!/usr/bin/python

xs = [0.0 ,.25 ,.5 , .75]
fxs = [1.0, 1.64872, 2.71828, 4.48169]
x = .43

def main():
	for i in xrange(3):
		degree = i+1
		print "degree ", degree
		p = 0
		for j in xrange(degree):
			p += fxs[j]*L(degree, j)
		print p

def L(n, k):
	i = 1
	for l in xrange(n):
		if not l == k:
			i *= (x - xs[l])/(xs[k] - xs[l])
	return i

if __name__ == '__main__':
	main()
