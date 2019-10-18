#!/usr/bin/python

def count_substring(string, sub_string):
    #count = string.count(sub_string)
    #return count
    #import regex as re
    #return len(re.findall(sub_string, string, overlapped=True))
    count = start = 0
    while True:
        start = string.find(sub_string, start) + 1
        if start > 0:
            count+=1
        else:
            return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
