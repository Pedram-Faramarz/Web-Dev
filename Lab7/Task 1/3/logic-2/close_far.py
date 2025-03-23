def close_far(a, b, c):
    close = lambda x, y: abs(x - y) <= 1
    far = lambda x, y: abs(x - y) >= 2

    return ((close(a, b) and far(b, c) and far(a, c)) or 
            (close(a, c) and far(c, b) and far(a, b)))

# Test cases
print(close_far(1, 2, 10))  # → True
print(close_far(1, 2, 3))   # → False
print(close_far(4, 1, 3))   # → True
print(close_far(5, 6, 8))   # → True
print(close_far(3, 1, 2))   # → False
