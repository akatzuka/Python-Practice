#!/usr/bin/python
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([score,name])

    students.sort()
    a = [i for i in students if i[0] != students[0][0]]
    b = [j for j in a if j[0] == a[0][0]]
    b.sort(key=lambda x: x[1])

    for i in range(len(b)):
        print(b[i][1])

#list students holds inputed score and name pairs, then is sorted
#list a uses list comprehension to remove all instances of the lowest score from list a; lowest remaining score is now second-lowest score overall
#list b uses list comprehension to trim list a to only inclue scores equal to the second-lowest
#list b is then sorted alphabetically by students name using lamba to indicate sort by second element (score, name)
#finally names in list b are printed
