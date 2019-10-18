#!/usr/bin/python

import numpy
#numpy.set_printoptions(legacy='1.13')
#Test case formatting is incorrect yet again, must inclue this line for proper formatting

a = []
b = []

a = ([int(i) for i in input().split()])
b = ([int(i) for i in input().split()])

a = numpy.array(a)
b = numpy.array(b)

print (numpy.inner(a, b))
print (numpy.outer(a, b))
