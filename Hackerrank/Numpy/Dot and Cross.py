#!/usr/bin/python

import numpy

n = int(input())

a = []
b = []

for _ in range(n):
    a.append([int(i) for i in input().split()])
for _ in range(n):
    b.append([int(i) for i in input().split()])

a = numpy.array(a)
b = numpy.array(b)

print (numpy.dot(a, b))
