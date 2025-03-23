def end_other(a, b):
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)

# Test cases
print(end_other('Hiabc', 'abc'))  # → True
print(end_other('AbC', 'HiaBc'))  # → True
print(end_other('abc', 'abXabc'))  # → True
print(end_other('hello', 'lo'))  # → True
print(end_other('test', 'TEST'))  # → True
print(end_other('abc', 'def'))  # → False
