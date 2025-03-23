def front_back(s):
    if len(s) <= 1:
        return s  # If the string has 0 or 1 character, return it as is
    return s[-1] + s[1:-1] + s[0]  # Swap first and last character

# Test cases
print(front_back('code'))  # → 'eodc'
print(front_back('a'))     # → 'a'
print(front_back('ab'))    # → 'ba'
print(front_back('hello')) # → 'oellh'
print(front_back('xyz'))   # → 'zyx'
