def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

# Test cases
print(parrot_trouble(True, 6))  # → True
print(parrot_trouble(True, 7))  # → False
print(parrot_trouble(False, 6))  # → False
print(parrot_trouble(True, 21))  # → True
print(parrot_trouble(False, 23))  # → False
