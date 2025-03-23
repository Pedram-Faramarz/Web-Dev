def lone_sum(a, b, c):
    if a == b == c:
        return 0
    if a == b:
        return c
    if a == c:
        return b
    if b == c:
        return a
    return a + b + c

# Test cases
print(lone_sum(1, 2, 3))  # → 6
print(lone_sum(3, 2, 3))  # → 2
print(lone_sum(3, 3, 3))  # → 0
print(lone_sum(5, 5, 10)) # → 10
print(lone_sum(7, 8, 9))  # → 24
print(lone_sum(4, 4, 2))  # → 2
