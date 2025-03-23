# read input value

year = int(input())

# check if the year is a leap year 
if(year % 4 ==0 and year % 100 !=0 or year % 400 ==0):
    print('YES')
else:
    print('NO')
    