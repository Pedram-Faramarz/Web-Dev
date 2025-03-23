# read input values
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# print numbers in range [a, b] that give remainder c when divided by d

for num in range(a, b+1):
    if num % d == c:
        print(num, end=' ')
        