def make_bricks(small, big, goal):
    max_big = min(big, goal // 5)  # Maximum big bricks that can be used
    remaining = goal - (max_big * 5)  # Remaining length to be covered with small bricks
    return remaining <= small  # Check if we have enough small bricks

# Test cases
print(make_bricks(3, 1, 8))  # → True
print(make_bricks(3, 1, 9))  # → False
print(make_bricks(3, 2, 10)) # → True
print(make_bricks(0, 3, 15)) # → True
print(make_bricks(1, 4, 12)) # → False
print(make_bricks(6, 2, 7))  # → True
