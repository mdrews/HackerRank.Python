n = int(input())
arr = map(int, input().split())

second = sorted(set(arr))[-2]
print(second)