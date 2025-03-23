def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

# Test cases
print(near_hundred(93))  # → True
print(near_hundred(90))  # → True
print(near_hundred(89))  # → False
print(near_hundred(110)) # → True
print(near_hundred(111)) # → False
print(near_hundred(190)) # → True
print(near_hundred(189)) # → False
print(near_hundred(200)) # → True
print(near_hundred(210)) # → True
print(near_hundred(211)) # → False
