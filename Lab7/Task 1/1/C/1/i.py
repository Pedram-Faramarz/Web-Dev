x = int(input())

count = 0

# loop from 1 to x and check for divisibility
for i in range(1, int(x ** 0.5)+1):
    if x % i == 0:
        count += 1 if i ==x//i else 2
print(count)