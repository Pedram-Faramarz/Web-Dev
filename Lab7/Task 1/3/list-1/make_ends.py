def make_ends(nums):
    return [nums[0], nums[-1]]

# Test cases
print(make_ends([1, 2, 3]))      # → [1, 3]
print(make_ends([1, 2, 3, 4]))   # → [1, 4]
print(make_ends([7, 4, 6, 2]))   # → [7, 2]
