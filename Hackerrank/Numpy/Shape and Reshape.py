#!/usr/bin/python

import numpy

arr = input().strip().split(' ')
arr = numpy.array(arr, dtype=int)
arr = arr.reshape(3, 3)
print (arr)
