def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10

# Test cases
print(in1to10(5, False))  # → True
print(in1to10(11, False)) # → False
print(in1to10(11, True))  # → True
print(in1to10(1, True))   # → True
print(in1to10(10, False)) # → True
print(in1to10(0, True))   # → True
