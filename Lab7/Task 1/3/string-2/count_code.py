import re

def count_code(s):
    return len(re.findall(r'co.e', s))

# Test cases
print(count_code('aaacodebbb'))  # → 1
print(count_code('codexxcode'))  # → 2
print(count_code('cozexxcope'))  # → 2
print(count_code('coae coze code cope'))  # → 4
print(count_code('nothing here'))  # → 0
