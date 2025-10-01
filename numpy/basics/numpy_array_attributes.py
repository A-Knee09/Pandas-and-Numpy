import numpy as np

# Array attributes

a1 = np.arange(10)
a2 = np.arange(12, dtype=float).reshape(3, 4)
a3 = np.arange(8).reshape(2, 2, 2)

# ndim: Returns the Dimension of an array

print(f"Dimension of a1 is: {a1.ndim}")
print(f"Dimension of a2 is: {a2.ndim}")
print(f"Dimension of a3 is: {a3.ndim}\n")

# shape : Returns the row and column count

print(f"a2: {a2}")
print(f"shape of a2: {a2.shape}\n")

# size: Returns the number of elements in the array

print(f"Size (No. of elements) of a1: {a1.size}")
print(f"Size (No. of elements) of a2: {a2.size}")
print(f"Size (No. of elements) of a3: {a3.size}\n")

# itemsize: Returns the byte size of an item in array, i.e how much size is one item occupying in the memory

print(f"Itemsize of a1: {a1.itemsize}")
print(f"Itemsize of a2: {a1.itemsize}")
print(f"Itemsize of a3: {a1.itemsize}\n")

# dtype: Data type of the items in the array

print(f"Data type of a1: {a1.dtype}")
print(f"Data type of a2: {a2.dtype}")
print(f"Data type of a3: {a3.dtype}\n")

# astype : Changing the datatype
print(f"Data type of a3: {a3.dtype}")
a4 = a3.astype(np.int32)
print(f"Data type of a3 after converting to int32 instead of int64: {a4.dtype}")
