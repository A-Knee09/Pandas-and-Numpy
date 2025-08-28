import numpy as np

a1 = np.arange(12).reshape(3, 4)
a2 = np.arange(12, 24).reshape(3, 4)

print(f"a1\n{a1}\n")
print(f"a2\n{a2}\n")

# Scaler Operations: You can add, subtract, multiply, or divide an entire NumPy array by a scalar (a single number) directly.

print(f"a1 elements multiplied by 2\n{a1 * 2}\n")
print(f"a1 elements added by 2\n{a1 + 2}\n")
print(f"a1 elements subtracted by 2\n{a1 - 2}\n")
print(f"a1 elements divided by 2\n{a1 / 2}\n")

# Relational Operations: Comparision operations between elements of the array, (<,>,==,!=,<=,>=)
print(f"Is every element greater than 15 in a2:\n{a2 > 15}\n")

# Vector Operations: Operations performed on arrays (+,-,*,**,/,...)

print(f"a1\n{a1}\n")
print(f"a2\n{a2}\n")
a3 = a1 + a2
print(f"a1 + a2:\n{a3}")
