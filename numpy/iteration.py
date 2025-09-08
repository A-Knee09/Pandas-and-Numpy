import numpy as np


a1 = np.arange(10)
a2 = np.arange(12).reshape(3, 4)
a3 = np.arange(27).reshape(3, 3, 3)


print(f"A1\n{a1}\n")
print(f"A2\n{a2}\n")
print(f"A3\n{a3}\n")


# Normal iteration in 1D
print("Iteration of A1 [1D array]")
for i in a1:
    print(i, end=" ")

print("")

# Iteration for the vector using the above will print rows (each 1D array in the vector)
print("\nIteration of Vector A2: ")
for i in a2:
    print(f"{i}\n")

# Iteration for a tensor using the above will print each vector
print("Iteration in Tensor A3")
for i in a3:
    print(f"{i}\n")

# Iteration using nditer method will convert everything to 1D and print elements indivisually
print("Iteration of Tensor A3 using nditer method")
for i in np.nditer(a3):
    print(i)
