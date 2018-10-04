from collections import OrderedDict
dict = OrderedDict()
for x in range(int(input())):
    item, space, value = input().rpartition(' ')
    if dict.get(item):
        dict[item] = dict[item] + int(value)
    else:
        dict[item] = int(value)
for key, value in dict.items():
    print(key + " " + str(value))