#!/usr/bin/python

import numpy

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append([int(i) for i in input().split()])

arr = numpy.array(arr)
arr = numpy.sum(arr, axis = 0)

print(numpy.prod(arr))
