#!/usr/bin/python

import numpy

#n,m = map(int, input().split())

#print (numpy.eye(n, m, k = 0)) #Test cases are broken, this is correct, however the elements in the test cases are shifted by one space to the right
print(str(numpy.eye(*map(int,input().split()))).replace('1',' 1').replace('0',' 0'))
