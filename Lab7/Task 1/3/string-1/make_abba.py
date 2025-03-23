def make_abba(a, b):
    return a + b + b + a

# Test cases
print(make_abba('Hi', 'Bye'))    # → 'HiByeByeHi'
print(make_abba('Yo', 'Alice'))  # → 'YoAliceAliceYo'
print(make_abba('What', 'Up'))   # → 'WhatUpUpWhat'
