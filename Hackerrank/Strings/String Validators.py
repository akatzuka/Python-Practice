#!/usr/bin/python

def is_num(s):
    a = any([c.isalnum() for c in s])
    print (a)
def is_alpha(s):
    a = any([c.isalpha() for c in s])
    print (a)
def is_digit(s):
    a = any([c.isdigit() for c in s])
    print (a)
def is_lower(s):
    a = any([c.islower() for c in s])
    print (a)
def is_upper(s):
    a = any([c.isupper() for c in s])
    print (a)

if __name__ == '__main__':
    s = input()
    is_num(s)
    is_alpha(s)
    is_digit(s)
    is_lower(s)
    is_upper(s)
