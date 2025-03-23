def array123(nums):
    for i in range(len(nums) - 2):  # Loop through the array until the third last element
        if nums[i:i+3] == [1, 2, 3]:  # Check if the slice matches [1, 2, 3]
            return True
    return False

# Test cases
print(array123([1, 1, 2, 3, 1]))  # → True
print(array123([1, 1, 2, 4, 1]))  # → False
print(array123([1, 1, 2, 1, 2, 3]))  # → True
print(array123([1, 2, 3, 4, 5]))  # → True
print(array123([3, 2, 1, 2, 3]))  # → True (sequence appears later)
print(array123([1, 2]))  # → False (sequence is incomplete)
