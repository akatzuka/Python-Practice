#!/usr/bin/python

import numpy

n,m,p = map(int,input().split())

arr_1 = []
arr_2 = []
for _ in range(n):
    arr_1.append([int(i) for i in input().split()])
for _ in range(m):
    arr_2.append([int(i) for i in input().split()])

arr_1 = numpy.array(arr_1)
arr_2 = numpy.array(arr_2)

print (numpy.concatenate((arr_1, arr_2), axis = 0))
