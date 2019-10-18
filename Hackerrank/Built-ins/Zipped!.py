#!/usr/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, x = map(int, input().split())    #reads N and X
scores = [map(float, input().split()) for _ in range(x)]    #reads in each line of scores

[print(sum(student)/x) for student in zip(*scores)]         #prints out average score for each element in scores
