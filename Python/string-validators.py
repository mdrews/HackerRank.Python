if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    dig = False
    lower = False
    upper = False
    for index in s:
        if s.isalnum() is True: alnum = True
        if s.isalpha() is True: alpha = True
        if s.isdigit() is True: dig = True
        if s.islower() is True: lower = True
        if s.isupper() is True: upper = True
    print(alnum)
    print(alpha)
    print(dig)
    print(lower)
    print(upper)