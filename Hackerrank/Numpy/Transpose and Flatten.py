#!/usr/bin/python

import numpy

n, m = input().split()
arr = []

for _ in range(int(n)):
    arr.append([int(i) for i in input().split()])

arr = numpy.array(arr)
print (numpy.transpose(arr))
print (arr.flatten())
