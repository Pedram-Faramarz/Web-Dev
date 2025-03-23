import math

# Read input values
a = int(input())
b = int(input())

# print perfect squares in the range
for num in range(a, b+1):
    if math.isqrt(num) ** 2 == num:
        print(num, end=' ')