N = int(input().strip())  # Read the number of elements
arr = list(map(int, input().strip().split()))  # Read the array elements

# Reverse the array in place
for i in range(N // 2):
    arr[i], arr[N - 1 - i] = arr[N - 1 - i], arr[i]

# Print the reversed array
print(" ".join(map(str, arr)))
