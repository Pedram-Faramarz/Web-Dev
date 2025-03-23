def string_bits(s):
    return s[::2]  # Slice the string to take every other character

# Test cases
print(string_bits('Hello'))      # → 'Hlo'
print(string_bits('Hi'))         # → 'H'
print(string_bits('Heeololeo'))  # → 'Hello'
print(string_bits('abcdef'))     # → 'ace'
print(string_bits('a'))          # → 'a'
print(string_bits(''))           # → ''
