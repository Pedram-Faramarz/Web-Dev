N = int(input().strip())  # Read the number of elements
arr = list(map(int, input().strip().split()))  # Read the array elements

# Count elements greater than the previous one
count = sum(1 for i in range(1, N) if arr[i] > arr[i - 1])

# Print the result
print(count)