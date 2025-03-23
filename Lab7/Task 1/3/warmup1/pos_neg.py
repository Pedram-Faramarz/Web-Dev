def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0  # Both must be negative if "negative" is True
    return (a < 0 and b > 0) or (a > 0 and b < 0)  # One negative, one positive

# Test cases
print(pos_neg(1, -1, False))  # → True
print(pos_neg(-1, 1, False))  # → True
print(pos_neg(-4, -5, True))  # → True
print(pos_neg(-4, -5, False)) # → False
print(pos_neg(1, 2, False))   # → False
print(pos_neg(-1, -1, True))  # → True
print(pos_neg(1, -1, True))   # → False
print(pos_neg(-1, 1, True))   # → False
