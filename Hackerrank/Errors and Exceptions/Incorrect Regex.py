#!/usr/bin/python

import re

for i in range(int(input())):
    try:
        re.compile(input().strip())
        print (True)
    except re.error:
        print (False)
