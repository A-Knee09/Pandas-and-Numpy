import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3, 4)
a3 = np.arange(27).reshape(3, 3, 3)

print(f"A1\n{a1}\n")
print(f"A2\n{a2}\n")
print(f"A3\n{a3}\n")

# For 1D (Vector) indexing is the same as lists in python
print(f"A1 : {a1[2]}")

# For 2D (Matrix) indexing is a2[row,column]
print(f"A2 : {a2[1, 3]}")
print(f"A2 : {a2[2, 0]}")

# For 3D (Tensor) indexing takes three value a3[which matrix][row][column]
print(f"A3 : {a3[1, 0, 1]}")
print(f"A3 : {a3[0, 1, 0]}")

# Slicing

# For vector its the same as list

# For matrix 2 args : a2[row,col] -> row and col themselves can be sliced
print(a2[0, :])  # Prints the first row, and all columns
print(f"{a2[:, 2]}\n")  # Prints 3rd column

"""
Prints 
[[5, 6]
 [9,10]]
"""
print(f"{a2[1:, 1:3]}\n")

"""
[[0,3]
 [8,11]]
"""
print(f"{a2[::2, ::3]}\n")

"""
[1, 3]
[9,11]
"""
print(a2[::2, 1::2])


# For tensors its the similar concept a3[matrix][row][col]
print(f"{a3[1]}\n")  # Prints the second matrix
print(f"{a3[1,:,1]}\n")  # Prints the second col of second matrix

print(f"{a3[::2]}\n")  # Prints 1st and last matrix

"""
[0,2]
[18,20]
"""

print(f"{a3[::2,0,::2]}")
