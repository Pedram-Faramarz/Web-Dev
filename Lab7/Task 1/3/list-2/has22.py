def has22(nums):
    for i in range(len(nums) - 1):  # Iterate up to second last index
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False

# Test cases
print(has22([1, 2, 2]))  # → True
print(has22([1, 2, 1, 2]))  # → False
print(has22([2, 1, 2]))  # → False
print(has22([2, 2, 2, 2]))  # → True
print(has22([1, 3, 2, 2, 5]))  # → True
print(has22([]))  # → False
print(has22([2]))  # → False
