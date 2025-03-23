# read input values
a = int(input())
b = int(input())

# print even numbers in the range 
for num in range(a, b+1):
    if num % 2 == 0:
        print(num, end=' ')