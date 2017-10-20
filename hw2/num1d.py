import numpy as np

def d(x, f):
	n = len(x) -1
	F = np.zeros((n+1, n+1))
	for i in xrange(len(f)):
		F[i][0] = f[i]

	for i in xrange(n):
		for j in xrange(i+1):
			if not x[i+1] - x[i-(j+1)] == 0:
				F[i+1][j+1] = (F[i+1][j]-F[i][j])/(x[i+1]-x[i-(j+1)])
			else:
				F[i+1][j+1] = (F[i+1][j]-F[i][j])/(x[i+1]-x[i-j+1])
	return F

x = [0., .25, .5, .75]
f = [1, 1.64872, 2.71828, 4.48169]
print d(x, f)

