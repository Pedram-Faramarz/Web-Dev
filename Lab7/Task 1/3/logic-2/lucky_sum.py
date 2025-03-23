def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c

# Test cases
print(lucky_sum(1, 2, 3))   # → 6
print(lucky_sum(1, 2, 13))  # → 3
print(lucky_sum(1, 13, 3))  # → 1
print(lucky_sum(13, 2, 3))  # → 0
print(lucky_sum(10, 13, 5)) # → 10
print(lucky_sum(5, 6, 7))   # → 18
