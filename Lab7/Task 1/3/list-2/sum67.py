def sum67(nums):
    total = 0
    ignore = False  # Flag to track whether we're inside a 6-7 section

    for num in nums:
        if num == 6:
            ignore = True  # Start ignoring numbers
        elif ignore and num == 7:
            ignore = False  # Stop ignoring numbers
        elif not ignore:
            total += num  # Add number to sum only if not ignored

    return total

# Test cases
print(sum67([1, 2, 2]))  # → 5
print(sum67([1, 2, 2, 6, 99, 99, 7]))  # → 5
print(sum67([1, 1, 6, 7, 2]))  # → 4
print(sum67([6, 7, 1, 2, 6, 3, 7, 4]))  # → 7
print(sum67([6, 7, 6, 7, 6, 7]))  # → 0
print(sum67([]))  # → 0
