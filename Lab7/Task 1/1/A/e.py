# read input values
v = int(input())
t = int(input())

# length of the MKAD
l = 109

# Calculate the distance
distance = (v * t) % l

# print the result
print(distance if distance >= 0 else l + distance)

