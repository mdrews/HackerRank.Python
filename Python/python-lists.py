if __name__ == '__main__':
    my_list = []
    N = int(input())
    for token in range(N):
        token = input().split()
        if token[0] == 'insert':
            my_list.insert(int(token[1]), int(token[2]))
        elif token[0] == 'print':
            print(token)
        elif token[0] == 'remove':
            my_list.remove(int(token[1]))
        elif token[0] == 'append':
            my_list.append(int(token[1]))
        elif token[0] == 'sort':
            my_list.sort()
        elif token[0] == 'pop':
            my_list.pop()
        elif token[0] == 'reverse':
            my_list.reverse()