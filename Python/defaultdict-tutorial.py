from collections import defaultdict
tokens = input().split()
a = []
b = []
i = 1
for x in range(int(tokens[0])):
    a.append(input())
for x in range(int(tokens[1])):
    b.append(input())
c = defaultdict(list)
for k in a:
    c.setdefault(k, []).append(i)
    i += 1
for key in b:
    if len(c[key]) == 0:
        print(-1)
    else:
        print(*c[key], sep=' ')