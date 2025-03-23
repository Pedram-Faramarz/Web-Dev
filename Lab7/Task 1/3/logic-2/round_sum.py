def round10(num):
    return (num + 5) // 10 * 10

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

# Test cases
print(round_sum(16, 17, 18))  # → 60
print(round_sum(12, 13, 14))  # → 30
print(round_sum(6, 4, 4))     # → 10
print(round_sum(25, 35, 45))  # → 110
print(round_sum(19, 21, 30))  # → 70
