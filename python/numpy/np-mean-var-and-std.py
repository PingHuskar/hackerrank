# Python > Numpy > Mean, Var, and Std
# Use the mean, var and std tools in NumPy on the given 2-D array.
#
# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
#

import numpy

n, m = map(int, input().split())
A = numpy.array([input().split() for i in range(n)], numpy.int)

print(numpy.mean(A, axis=1))
print(numpy.var(A, axis=0))
print(round(numpy.std(A, axis=None),11))
