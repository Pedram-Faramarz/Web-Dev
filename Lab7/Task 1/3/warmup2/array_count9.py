def array_count9(nums):
    return nums.count(9)

# Test cases
print(array_count9([1, 2, 9]))        # → 1
print(array_count9([1, 9, 9]))        # → 2
print(array_count9([1, 9, 9, 3, 9]))  # → 3
print(array_count9([1, 2, 3, 4]))     # → 0
print(array_count9([9, 9, 9, 9, 9]))  # → 5
