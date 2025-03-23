def sleep_in(weekday, vacation):
    return not weekday or vacation

# Test cases
print(sleep_in(False, False))  # → True
print(sleep_in(True, False))   # → False
print(sleep_in(False, True))   # → True
print(sleep_in(True, True))    # → True
