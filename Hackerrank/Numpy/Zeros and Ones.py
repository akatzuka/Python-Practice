#!/usr/bin/python

import numpy

n = [int(i) for i in input().split()]

print (numpy.zeros(tuple(n), dtype=int))
print (numpy.ones(tuple(n), dtype=int))
