#!/usr/bin/python

import numpy

numpy.set_printoptions(sign=' ')   #Need to set this since the test cases have broken white spacing

a=[float(i) for i in input().split()]

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
