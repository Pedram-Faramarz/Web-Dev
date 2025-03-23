def count_hi(s):
    return s.count("hi")

# Test cases
print(count_hi('abc hi ho'))  # → 1
print(count_hi('ABChi hi'))   # → 2
print(count_hi('hihi'))       # → 2
print(count_hi('hiHIHi'))     # → 1 (case-sensitive)
print(count_hi('hihihihi'))   # → 4
