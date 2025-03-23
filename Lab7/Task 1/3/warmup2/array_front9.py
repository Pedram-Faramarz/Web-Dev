def array_front9(nums):
    return 9 in nums[:4]

# Test cases
print(array_front9([1, 2, 9, 3, 4]))  # → True
print(array_front9([1, 2, 3, 4, 9]))  # → False
print(array_front9([1, 2, 3, 4, 5]))  # → False
print(array_front9([9, 2, 3]))        # → True (array has less than 4 elements but contains 9)
print(array_front9([]))               # → False (empty array)
