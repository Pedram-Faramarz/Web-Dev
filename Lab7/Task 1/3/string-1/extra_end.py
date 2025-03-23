def extra_end(s):
    return s[-2:] * 3

# Test cases
print(extra_end('Hello'))  # → 'lololo'
print(extra_end('ab'))     # → 'ababab'
print(extra_end('Hi'))     # → 'HiHiHi'
