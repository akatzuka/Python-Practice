#!/usr/bin/python
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/len(query_scores)))
    #"{0:.2f}".format is needed for proper rounding for test cases
