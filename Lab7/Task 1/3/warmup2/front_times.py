def front_times(s, n):
    front = s[:3]  # Get the first 3 characters (or fewer if the string is shorter)
    return front * n  # Repeat the front n times

# Test cases
print(front_times('Chocolate', 2))  # → 'ChoCho'
print(front_times('Chocolate', 3))  # → 'ChoChoCho'
print(front_times('Abc', 3))        # → 'AbcAbcAbc'
print(front_times('A', 4))          # → 'AAAA'
print(front_times('Hi', 5))         # → 'HiHiHiHiHi'
print(front_times('', 3))           # → ''
