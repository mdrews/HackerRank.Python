from collections import deque
tokens = input()
d = deque()
for command in range(int(tokens)):
    command = input().split()
    if command[0] == 'append':
        d.append(command[1])
    if command[0] == 'appendleft':
        d.appendleft(command[1])
    if command[0] == 'pop':
        d.pop()
    if command[0] == 'popleft':
        d.popleft()
print(*d, sep=' ')