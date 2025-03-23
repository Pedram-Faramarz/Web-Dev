import sys

# read 100 numbers from standart input

numbers = map(int, sys.stdin.read().split())    

print(sum(numbers))