tests = int(input())
for test in range(tests):
    arr_length = int(input())
    arr = list(map(int, input().split()))
    left_index = 0
    right_index = len(arr)-1
    while left_index < len(arr)-2 and arr[left_index] >= arr[left_index+1]:
        left_index += 1
    while right_index > 0 and arr[right_index] >= arr[right_index-1]:
        right_index -= 1
    print('Yes') if right_index - left_index <= 1 else print('No')