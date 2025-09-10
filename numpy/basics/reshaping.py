import numpy as np

a1 = np.arange(0, 12).reshape((3, 4))

print(f"A1 matrix:\n{a1}\n")

# transpose : Convert the rows to columns and visa versa
print(f"A1 Transpose\n")
print(f"{np.transpose(a1)}\n")

# or
# print(a1.T)

# Ravel : Convert n dimension array to 1D
a3 = np.arange(24).reshape((2, 4, 3))
print(f"A3 Tensor\n{a3}\n")

print(f"Tensor ravel\n{a3.ravel()}")
