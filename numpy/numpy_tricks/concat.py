import numpy as np


# Concat : Join two arrays, works similar to hstack and vstack

a = np.arange(0, 6).reshape(2, 3)
b = np.arange(6, 12).reshape(2, 3)

print(f"Matrix A\n{a}\n")
print(f"Matrix B\n{b}\n")

print(f"Concatenated Horizontally\n{np.concatenate((a,b),axis=1)}\n")
print(f"Concatenated Vertically\n{np.concatenate((a,b),axis=0)}\n")

# Unique: Finds a unique element

a = np.array([1, 1, 1, 2, 2, 2, 6, 4, 4, 4])
print(np.unique(a))
