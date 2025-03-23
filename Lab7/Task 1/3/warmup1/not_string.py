def not_string(s):
    if s.startswith("not"):  # Check if the string already starts with "not"
        return s
    return "not " + s  # Add "not " at the beginning if not already present

# Test cases
print(not_string('candy'))    # → 'not candy'
print(not_string('x'))        # → 'not x'
print(not_string('not bad'))  # → 'not bad'
print(not_string('notebook')) # → 'notebook'
print(not_string('bad'))      # → 'not bad'
