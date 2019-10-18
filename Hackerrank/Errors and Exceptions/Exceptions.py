#!/usr/bin/python

for i in range(int(input())):
    try:
        x, y = map(int, input().split())
        print (x//y)
    except ValueError as o:
        print ("Error Code: " +str(o))
    except ZeroDivisionError as o:
        print ("Error Code: " +str(o))
