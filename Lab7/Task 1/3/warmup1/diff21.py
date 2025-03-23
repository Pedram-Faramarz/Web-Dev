def diff21(n):
    if n > 21:
        return 2 * abs(n - 21)
    return abs(n - 21)

# Test cases
print(diff21(19))  # → 2
print(diff21(10))  # → 11
print(diff21(21))  # → 0
print(diff21(25))  # → 8
print(diff21(30))  # → 18
