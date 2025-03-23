def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Read input and call the function
year = int(input())  # Read an integer input for the year
print(is_leap(year))  # Print the boolean result
