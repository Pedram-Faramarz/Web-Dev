def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]

# Test cases
print(rotate_left3([1, 2, 3]))     # → [2, 3, 1]
print(rotate_left3([5, 11, 9]))    # → [11, 9, 5]
print(rotate_left3([7, 0, 0]))     # → [0, 0, 7]
