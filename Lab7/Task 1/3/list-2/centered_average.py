def centered_average(nums):
    nums.sort()  # Sort the list in ascending order
    return sum(nums[1:-1]) // (len(nums) - 2)  # Remove min & max, then compute average

# Test cases
print(centered_average([1, 2, 3, 4, 100]))  # → 3
print(centered_average([1, 1, 5, 5, 10, 8, 7]))  # → 5
print(centered_average([-10, -4, -2, -4, -2, 0]))  # → -3
print(centered_average([2, 3, 4, 5, 6]))  # → 4
print(centered_average([6, 1, 2, 3, 4]))  # → 3
