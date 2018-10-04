n = int(input())
arr = map(int, input().split())

first = 0
second = 0
for n in arr:
    if n > first or n > second:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n
print(second)