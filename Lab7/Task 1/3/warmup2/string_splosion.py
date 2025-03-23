def string_splosion(s):
    result = ""
    for i in range(len(s) + 1):
        result += s[:i]  # Add the substring from start to i
    return result

# Test cases
print(string_splosion('Code'))  # → 'CCoCodCode'
print(string_splosion('abc'))   # → 'aababc'
print(string_splosion('ab'))    # → 'aab'
print(string_splosion('x'))     # → 'x'
print(string_splosion('xyz'))   # → 'xxyxyz'
