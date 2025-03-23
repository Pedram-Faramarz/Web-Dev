def double_char(s):
    return ''.join([char * 2 for char in s])

# Test cases
print(double_char('The'))       # → 'TThhee'
print(double_char('AAbb'))      # → 'AAAAbbbb'
print(double_char('Hi-There'))  # → 'HHii--TThheerree'
print(double_char('123'))       # → '112233'
print(double_char('!@#'))       # → '!!@@##'
