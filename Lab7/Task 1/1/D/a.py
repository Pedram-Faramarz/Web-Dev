N = int(input())

arr = list(map(int, input().split()))

print(" ".join(map(str, arr[0:N:2])))