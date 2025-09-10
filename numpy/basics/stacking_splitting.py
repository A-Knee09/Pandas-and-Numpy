import numpy as np

a1 = np.arange(12).reshape((3, 4))
a2 = np.arange(12, 24).reshape((3, 4))

print(f"A1 matrix\n{a1}\n")
print(f"A2 matrix\n{a2}\n")


# Horizontal stacking : Shape should be the same
print(f"Stacking A1 and A2 matrix Horizontally\n{np.hstack((a1,a2))}\n")

# Vertical Stacking
print(f"Stacking A1 and A2 matrix Vertically\n{np.vstack((a1,a2))}\n")

# Horizontal Split: Cut the array Horizontally
print(f"A1 matrix Horizontally split in two\n{np.hsplit(a1,2)}\n")

# Vertical Split: Cut the array Vertically
print(f"A1 matrix Vertically split in three\n{np.vsplit(a1,3)}")
