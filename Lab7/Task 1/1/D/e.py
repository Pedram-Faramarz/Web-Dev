N = int(input().strip())  # Read the number of elements
arr = list(map(int, input().strip().split()))  # Read the array elements

# Check for adjacent elements with the same sign
found = any(arr[i] * arr[i - 1] > 0 for i in range(1, N))

# Print the result
print("YES" if found else "NO")
