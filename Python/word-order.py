from collections import OrderedDict
words = int(input())
d = OrderedDict()
for w in range(words):
    key = input()
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
print(len(d))
print(*d.values(), sep=' ')