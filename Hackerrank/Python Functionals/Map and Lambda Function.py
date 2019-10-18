#!/usr/bin/python

cube = lambda x: x*x*x

def fibonacci(n):
    fib = []
    for i in range(n):
        if (i==0):
            fib.append(0)
        elif (i==1):
            fib.append(1)
        else:
            fib.append(fib[i-1] + fib[i-2])
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
