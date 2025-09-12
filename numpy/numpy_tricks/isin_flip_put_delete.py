import numpy as np


# isin: used to test whether each element of a NumPy array is present in a second array of test elements. It returns a boolean array of the same shape as the first input array, where True indicates that the corresponding element was found in the second array, and False indicates it was not

a = np.array([20, 13, 4, 24, 12, 38, 85, 83, 94, 7])
b = np.random.randint(1, 100, 12).reshape(3, 4)
items = [1, 20, 4, 9, 7]

print(f"A\n{a}\n")
print(f"items\n{items}\n")
print(f"{np.isin(a, items)}\n")
print(f"{a[np.isin(a, items)]}\n")

# flip: Reverses the array along a specified axis while preserving shape

print(f"Flipped array A\n{np.flip(a)}")

print(f"Matrix B\n{b}\n")
print(f"Flipped row and column wise\n{np.flip(b)}\n")
print(f"Flipped row wise\n{np.flip(b,axis=1)}\n")
print(f"Flipped column wise\n{np.flip(b,axis=0)}\n")

# Put: Change multiple items , np.put(array , [index(s)] , [item(s)])

np.put(a, [0, 1], [100, 200])
print(f"New array A\n{a}\n")

# Delete : returns a new array with deletion of sub arrays along mentioned axis

print(f"{np.delete(a, [0, 2, 4])}\n")
