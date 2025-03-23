def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

# Test cases
print(monkey_trouble(True, True))   # → True
print(monkey_trouble(False, False)) # → True
print(monkey_trouble(True, False))  # → False
print(monkey_trouble(False, True))  # → False
