def first_half(s):
    return s[:len(s)//2]

# Test cases
print(first_half('WooHoo'))      # → 'Woo'
print(first_half('HelloThere'))  # → 'Hello'
print(first_half('abcdef'))      # → 'abc'
