x = int(input())

# loop from 1 to x and check for divisibility
for i in range(1, x+1):
    if x % i == 0:
        print(i, end=' ')
        