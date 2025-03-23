def front3(s):
    front = s[:3]  # Get the first 3 characters (or the whole string if it's shorter)
    return front * 3  # Repeat it 3 times

# Test cases
print(front3('Java'))      # → 'JavJavJav'
print(front3('Chocolate')) # → 'ChoChoCho'
print(front3('abc'))       # → 'abcabcabc'
print(front3('ab'))        # → 'ababab'
print(front3('a'))         # → 'aaa'
print(front3(''))          # → ''
