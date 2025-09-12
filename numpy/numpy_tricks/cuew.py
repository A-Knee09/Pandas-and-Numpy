import numpy as np


# Concat : Join two arrays, works similar to hstack and vstack

a = np.arange(0, 6).reshape(2, 3)
b = np.arange(6, 12).reshape(2, 3)

print(f"Matrix A\n{a}\n")
print(f"Matrix B\n{b}\n")

print(f"Concatenated Horizontally\n{np.concatenate((a,b),axis=1)}\n")
print(f"Concatenated Vertically\n{np.concatenate((a,b),axis=0)}\n")

# Unique : Finds a unique element

a = np.array([1, 1, 1, 2, 2, 2, 6, 4, 4, 4])
print(f"{np.unique(a)}\n")

# expand_dims : Expands the dimension , ex. 1D -> 2D, pretty useful sometimes

a = np.array([11, 23, 45, 10, 42])
print(f"{a}\n")

print(f"{np.expand_dims(a, axis=0)}\n")
print(f"{np.expand_dims(a, axis=0).shape}\n")
print(f"{np.expand_dims(a, axis=1)}\n")
print(f"{np.expand_dims(a, axis=1).shape}\n")

# where : Returns the indices of elements in an input array where the given condition is true
# np.where(condition,true,false) -> true means what to do if the condition is true and same for false
print(f"{a}\n")
print(f"{np.where(a>25)}\n")

print(f"{np.where(a > 25, 0, a)}\n")
