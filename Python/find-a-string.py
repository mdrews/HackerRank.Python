def count_substring(string, sub_string):
    result = 0
    for x in range(len(string)-len(sub_string)+1):
        if sub_string == string[x:x+len(sub_string)]:
            result += 1
    return result


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)