def makes10(a, b):
    return a == 10 or b == 10 or (a + b == 10)

# Test cases
print(makes10(9, 10))  # → True
print(makes10(9, 9))   # → False
print(makes10(1, 9))   # → True
print(makes10(10, 5))  # → True
print(makes10(5, 5))   # → True
print(makes10(7, 3))   # → True
print(makes10(4, 6))   # → True
print(makes10(2, 8))   # → True
print(makes10(0, 10))  # → True
print(makes10(0, 9))   # → False
