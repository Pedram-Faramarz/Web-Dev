def sum13(nums):
    total = 0
    skip_next = False  # Flag to track numbers right after 13

    for num in nums:
        if num == 13:
            skip_next = True  # Skip the next number
            continue
        if skip_next:
            skip_next = False  # Reset the flag and skip this number
            continue
        total += num

    return total

# Test cases
print(sum13([1, 2, 2, 1]))  # → 6
print(sum13([1, 1]))  # → 2
print(sum13([1, 2, 2, 1, 13]))  # → 6
print(sum13([13, 1, 2, 13, 2, 1]))  # → 3
print(sum13([]))  # → 0
print(sum13([13, 13, 2, 3]))  # → 3
