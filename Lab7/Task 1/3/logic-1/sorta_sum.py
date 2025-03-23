def sorta_sum(a, b):
    sum_ab = a + b
    if 10 <= sum_ab <= 19:
        return 20
    return sum_ab

# Test cases
print(sorta_sum(3, 4))   # → 7
print(sorta_sum(9, 4))   # → 20
print(sorta_sum(10, 11)) # → 21
