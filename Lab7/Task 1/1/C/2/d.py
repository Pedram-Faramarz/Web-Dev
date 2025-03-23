N = int(input())

power = 1

while power <= N:
    power *=2

print("YES" if power == N else "NO")