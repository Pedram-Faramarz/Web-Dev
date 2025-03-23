def sum2(nums):
    return sum(nums[:2]) if len(nums) >= 2 else sum(nums)

# Test cases
print(sum2([1, 2, 3]))    # → 3
print(sum2([1, 1]))       # → 2
print(sum2([1, 1, 1, 1])) # → 2
print(sum2([5]))          # → 5
print(sum2([]))           # → 0
