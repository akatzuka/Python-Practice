#!/usr/bin/python

import numpy

n,m = map(int,input().split())

a=[]
b=[]
for _ in range(n):
    a.append([int(i) for i in input().split()])

for _ in range(n):
    b.append([int(i) for i in input().split()])

a = numpy.array(a)
b = numpy.array(b)

print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(a//b)
print(numpy.mod(a,b))
print(numpy.power(a,b))
