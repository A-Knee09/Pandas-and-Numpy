import numpy as np

# argmax : Returns the indices of the max element of the array in a particular axis

a = np.random.randint(1, 100, 10)
b = np.random.randint(1, 100, 12).reshape(4, 3)

print(f"Random array\n{a}\n")
print(f"Random array\n{b}\n")

print(
    f"Highest value and index of the highest value : {a[np.argmax(a)]}, {np.argmax(a)}"
)

print(f"Index of the highest value column wise: {np.argmax(b,axis=0)}")
print(f"Index of the highest value row wise: {np.argmax(b,axis=1)}\n")

print(
    f"Smallest value and index of the Smallest value : {a[np.argmin(a)]}, {np.argmin(a)}"
)

print(f"Index of the smallest value column wise: {np.argmin(b,axis=0)}")
print(f"Index of the smallest value row wise: {np.argmax(b,axis=1)}")
