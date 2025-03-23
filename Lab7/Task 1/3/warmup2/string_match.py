def string_match(a, b):
    count = 0
    min_length = min(len(a), len(b))  # Find the length of the shorter string
    
    for i in range(min_length - 1):  # Iterate until the second last character
        if a[i:i+2] == b[i:i+2]:  # Compare two-character substrings
            count += 1
            
    return count

# Test cases
print(string_match('xxcaazz', 'xxbaaz'))  # → 3
print(string_match('abc', 'abc'))  # → 2
print(string_match('abc', 'axc'))  # → 0
print(string_match('aabbcc', 'aabbcc'))  # → 5
print(string_match('aabbcc', 'aabxcy'))  # → 3
