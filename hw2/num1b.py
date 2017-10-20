#!/usr/bin/python
import numpy as np

def main():
	xi = [0., .25, .5, .75]
	fi = [1, 1.64872, 2.71828, 4.48169]
	x = .43
	q = neville(x, xi, fi)
	print q

def neville(x, xi, fi):
	n = len(xi) - 1
	m = np.zeros((n+1, n+1))
	for i in xrange(len(fi)):
		m[i][0] = fi[i]
	for i in xrange(n):
		for j in xrange(i+1):
			if not xi[i+1]-xi[i-(j+1)] == 0:
				m[i+1][j+1] = ((x-xi[i-(j+1)])*m[i+1][j]-(x-xi[i+1])*m[i][j])/(xi[i+1]-xi[i-(j+1)])
			else: #this is an artifact of pythons odd indexing rules.
				m[i+1][j+1] = ((x-xi[i-(j)])*m[i+1][j]-(x-xi[i+1])*m[i][j])/(xi[i+1]-xi[i-(j)])

	return m

if __name__ == '__main__':
	main()
