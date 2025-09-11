import numpy as np

"""
Sort : Returns a sorted copy of an array
np.sort(a, axis=-1, kind=None, order=None, *, stable=None)
kind : {‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, optional
order : str or list of str, optional
"""

a = np.random.randint(1, 20, 10)
print(f"Random array\n{a}\n")
print(f"Sorted array using 'np.sort()'\n{np.sort(a)}\n")

b = np.random.randint(1, 100, 24).reshape(6, 4)
print(f"Random Matrix\n{b}\n")
print(f"Row wise matrix sort, axis = 1\n{np.sort(b)}\n")
print(f"Column wise matrix sort, axis = 0\n{np.sort(b,axis=0)}\n")

# Append: Add an element to the end
print(f"Appending on vector\n{np.append(a,500)}\n")

print(f"Appending ones in Matrix\n{np.append(b,np.ones((b.shape[0],1)),axis=1)}\n")
