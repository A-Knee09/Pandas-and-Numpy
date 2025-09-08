import numpy as np
import time
import sys

# Speed

# list

a = [i for i in range(1_00_00_000)]
b = [i for i in range(1_00_00_000, 2_00_00_000)]
c = []

start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])

print(f"Total time to add elements in lists: {time.time() -start} sec\n")


# Numpy array

x = np.arange(1_00_00_000)
y = np.arange(1_00_00_000, 2_00_00_000)

start = time.time()
z = x + y
print(f"Total time to add elements of two arrays in numpy: {time.time() - start} sec\n")

print(f"Memory used in bytes by list C: {sys.getsizeof(c)}\n")
print(f"Memory used in bytes by Numpy Z: {sys.getsizeof(z)}\n")
