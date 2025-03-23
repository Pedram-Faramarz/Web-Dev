
def missing_char(s, n):
    return s[:n] + s[n+1:]  # Remove the character at index n by slicing

# Test cases
print(missing_char('kitten', 1))  # → 'ktten'
print(missing_char('kitten', 0))  # → 'itten'
print(missing_char('kitten', 4))  # → 'kittn'
print(missing_char('hello', 2))   # → 'helo'
print(missing_char('python', 5))  # → 'pytho'
