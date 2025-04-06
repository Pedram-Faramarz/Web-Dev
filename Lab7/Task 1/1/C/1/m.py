N = int(input())

zero_count = sum(1 for _ in range(N) if int(input()) == 0)

print(zero_count)


