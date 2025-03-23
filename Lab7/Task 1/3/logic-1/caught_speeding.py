def caught_speeding(speed, is_birthday):
    # Increase speed limits by 5 if it's your birthday
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0  # No ticket
    elif speed <= 80:
        return 1  # Small ticket
    else:
        return 2  # Big ticket

# Test cases
print(caught_speeding(60, False))  # → 0
print(caught_speeding(65, False))  # → 1
print(caught_speeding(65, True))   # → 0
