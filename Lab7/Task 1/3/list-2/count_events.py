def count_evens(nums):
    return sum(1 for num in nums if num % 2 == 0)

# Test cases
print(count_evens([2, 1, 2, 3, 4]))  # → 3
print(count_evens([2, 2, 0]))  # → 3
print(count_evens([1, 3, 5]))  # → 0
print(count_evens([4, 6, 8, 10]))  # → 4
print(count_evens([]))  # → 0
