def combo_string(a, b):
    if len(a) < len(b):
        short, long = a, b
    else:
        short, long = b, a
    return short + long + short

# Test cases
print(combo_string('Hello', 'hi'))  # → 'hiHellohi'
print(combo_string('hi', 'Hello'))  # → 'hiHellohi'
print(combo_string('aaa', 'b'))     # → 'baaab'
