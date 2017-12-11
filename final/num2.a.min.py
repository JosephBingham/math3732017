#!/usr/bin/python
import random
import numpy as np

def inverseIteration(A, mu, maxIter):
	m = len(A)
	n = len(A[0])
	if not n == m:
		print 'input is not square'
		return
	q = np.random.rand(m)
	q /= np.linalg.norm(q)
	lam = 0
	w = None
	for i in xrange(maxIter):
		inter = A-mu*np.eye(m)
		w = np.linalg.solve(inter, q)
		q = w/np.linalg.norm(w)
		l1 = np.dot(q.T, A)
		lam = np.dot(l1, q)
	return lam, q

n = 20
A = 2*np.eye(n)
A -= np.eye(n, k = 1)
A -= np.eye(n, k = -1)
print inverseIteration(A, 0, 10000)[0]
