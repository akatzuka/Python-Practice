#!/usr/bin/python

import numpy

a = []
a = ([float(i) for i in input().split()])

x = int(input())

print (numpy.polyval(a, x))
#alt solution: print (numpy.polyval(a, int(input()))
