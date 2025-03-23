def find_min(a: int, b: int, c: int, d: int) -> int:
    return min(a, b, c, d)

# Read input
a, b, c, d = map(int, input().strip().split())

# Compute and print the minimum value
print(find_min(a, b, c, d))
