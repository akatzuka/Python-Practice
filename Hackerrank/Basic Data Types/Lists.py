#!/usr/bin/python
li = []

for i in range(int(input())):
    a = input().split()
    if a[0] == 'print':
        print (li)
    elif a[0] == 'index':
        print (li.index(int(a[1])))
    elif a[0] == 'count':
        print (li.count(int(a[1])))
    else:
        getattr(li,a[0])(*map(int,a[1:]))
