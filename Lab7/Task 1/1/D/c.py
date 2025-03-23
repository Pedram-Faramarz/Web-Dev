N = int(input().strip())  # Read the number of elements
arr = list(map(int, input().strip().split()))  # Read the array elements

# Count the number of positive numbers
positive_count = sum(1 for x in arr if x > 0)

# Print the result
print(positive_count)
