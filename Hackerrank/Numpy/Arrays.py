#!/usr/bin/python

import numpy

def arrays(arr):
    return numpy.array(numpy.flip(arr), dtype=float)

arr = input().strip().split(' ')
