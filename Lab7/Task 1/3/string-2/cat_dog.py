def cat_dog(s):
    return s.count("cat") == s.count("dog")

# Test cases
print(cat_dog('catdog'))         # → True
print(cat_dog('catcat'))         # → False
print(cat_dog('1cat1cadodog'))   # → True
print(cat_dog('catdogdogcat'))   # → True
print(cat_dog('dogcatcatdogdog')) # → False
