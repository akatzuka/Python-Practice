#!/usr/bin/python

def split_and_join(line):
    splitd = line.split()
    joind = "-".join(splitd)
    return joind

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
