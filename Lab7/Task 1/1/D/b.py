N = int(input())

arr = list(map(int, input().split()))

print(" ".join(map(str,[x for x in arr if x % 2 == 0])))