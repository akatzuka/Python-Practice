#!/usr/bin/python

import numpy
numpy.set_printoptions(legacy='1.13')
#Test case formatting is incorrect yet again, must inclue this line for proper formatting

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append([int(i) for i in input().split()])

arr = numpy.array(arr)

print (numpy.mean(arr, axis = 1))
print (numpy.var(arr, axis = 0))
print (numpy.std(arr, axis = None))
