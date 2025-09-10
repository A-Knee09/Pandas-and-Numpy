"""
Broadcasting in NumPy is a mechanism that allows arithmetic operations to be performed on arrays of different shapes and sizes. It enables element-wise operations without requiring explicit reshaping or duplication of data

When performing an operation between two arrays with different numbers of dimensions, NumPy implicitly prepends ones to the shape of the smaller-dimensional array until both arrays have the same number of dimensions.

The smaller array is 'broadcast' among the larger one so that they may have compatible shape.
"""

import numpy as np

a = np.arange(6).reshape(2, 3)
b = np.arange(3).reshape(1, 3)


print(f"Matrix A\n{a}\n")
print(f"Vector B\n{b}\n")


print(f"A+B\n{a+b}\n")

"""
NumPy Broadcasting Rules:

1. Compare shapes of arrays element-wise from the trailing dimensions.
2. Dimensions are compatible if:
   - They are equal, OR
   - One of them is 1.
3. If one dimension is 1, the array is virtually 'stretched' to match the other.
4. If dimensions mismatch and neither is 1 → broadcasting fails.
5. Resulting shape is the maximum along each dimension.

Examples:
- (5, 1) + (1, 4) -> (5, 4)
- (3, ) + (3, 3) -> (3, 3)
- (2, 3) + (2,) -> (2, 3)
"""
