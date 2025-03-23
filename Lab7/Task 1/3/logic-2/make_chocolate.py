def make_chocolate(small, big, goal):
    max_big_bars = min(goal // 5, big)  # Use as many big bars as possible without exceeding goal
    remaining_weight = goal - (max_big_bars * 5)  # Compute remaining weight needed

    if remaining_weight <= small:  # Check if we have enough small bars
        return remaining_weight
    else:
        return -1  # Not possible to reach the goal

# Test cases
print(make_chocolate(4, 1, 9))  # → 4
print(make_chocolate(4, 1, 10)) # → -1
print(make_chocolate(4, 1, 7))  # → 2
print(make_chocolate(6, 2, 7))  # → 2
print(make_chocolate(0, 3, 15)) # → 0
print(make_chocolate(1, 2, 6))  # → -1
