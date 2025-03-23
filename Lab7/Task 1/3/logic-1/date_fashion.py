def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0  # No table if either of you is too unstylish
    elif you >= 8 or date >= 8:
        return 2  # Guaranteed table if either of you is very stylish
    else:
        return 1  # Otherwise, it's a maybe

# Test cases
print(date_fashion(5, 10))  # → 2
print(date_fashion(5, 2))   # → 0
print(date_fashion(5, 5))   # → 1
