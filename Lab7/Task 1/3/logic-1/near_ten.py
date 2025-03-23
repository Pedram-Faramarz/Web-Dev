def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8

# Test cases
print(near_ten(12))  # → True
print(near_ten(17))  # → False
print(near_ten(19))  # → True
print(near_ten(20))  # → True
print(near_ten(8))   # → False
print(near_ten(29))  # → True
