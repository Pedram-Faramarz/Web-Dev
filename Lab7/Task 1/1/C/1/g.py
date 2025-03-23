import sys

# read the input number
x = int(sys.stdin.readline().strip())

# if x is even , the smallest divisor is 2
if x % 2 == 0:
    print(2)
else :
    for i in range (3, int(x ** 0.5)+ 1, 2):
        if x % i == 0:
            print(i)
            break
    else:
        print(x)
        