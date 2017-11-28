#!/usr/bin/python
from scipy import *

def lunopiv(A):
    m,n = shape(A)
    for i in arange(0,n):
        pivot = A[i,i]
        for k in arange(i+1,n):
            A[k,i] = A[k,i]/pivot
            A[k,i+1:n] = A[k,i+1:n] - A[k,i]*A[i,i+1:n]
    L = eye(n)+tril(A,-1)
    U = triu(A)
    return L,U

A = array([ [2, 3, -1], [4, 4, -1], [-2, -3, 4] ])

print lunopiv(A)
