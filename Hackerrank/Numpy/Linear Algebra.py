#!/usr/bin/python

import numpy
numpy.set_printoptions(legacy='1.13')
#Test case formatting is incorrect yet again, must inclue this line for proper formatting


n = int(input())

a = []
for _ in range(n):
    a.append([float(i) for i in input().split()])

a = numpy.array(a)

print (numpy.linalg.det(a))
