import numpy
def ldl(A):
	A = numpy.matrix(A)
	S = numpy.diag(numpy.diag(A))
	Sinv = numpy.diag(1/numpy.diag(A))
	D = numpy.matrix(S.dot(S))
	Lch = numpy.linalg.cholesky(A)
	L = numpy.matrix(Lch.dot(Sinv))
	return L, D

A = numpy.matrix([[2., -1., 0.], [-1., 2., -1.], [0., -1., 2.]])

L, D = ldl(A)

print L
print D
