def xyz_there(s):
    return 'xyz' in s.replace('.xyz', '')

# Test cases
print(xyz_there('abcxyz'))  # → True
print(xyz_there('abc.xyz'))  # → False
print(xyz_there('xyz.abc'))  # → True
print(xyz_there('x.xyzxyz'))  # → True
print(xyz_there('.xyzxyz'))  # → True
print(xyz_there('.xyz'))  # → False
print(xyz_there('xyz'))  # → True
