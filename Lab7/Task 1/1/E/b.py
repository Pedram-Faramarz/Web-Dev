def power(a: float, n: int) -> float:
    return a ** n

# Read input
a, n = map(float, input().strip().split())
n = int(n)  # Ensure n is an integer

# Compute and print the result
print(power(a, n))
