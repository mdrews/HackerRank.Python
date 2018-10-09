from collections import namedtuple
students = int(input())
identifiers = input().split()
marks = identifiers.index('MARKS')
sum = 0
for s in range(students):
    s = input().split()
    sum += int(s[marks])
print(sum/students)