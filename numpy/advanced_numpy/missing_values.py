# Working with missing values denoted by NaN (Not a Number)

import numpy as np

a = np.array([1, 2, 3, 4, np.nan, 6])

print(a)

# Converts the array to boolean array, with missing ones as true. We can use this as mask
np.isnan(a)

print(a[~(np.isnan(a))])  # Removes the nan values
