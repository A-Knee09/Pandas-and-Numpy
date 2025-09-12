import numpy as np

# Cumsum and cumprod : is used when you want to calculate cumlative sum/prod of array elements over a given axis. ex {1,2,3} -> {1,3,6}
# If no axis is provided the matrix or tensor is converted to vector

a = np.random.randint(0, 70, 11)
b = np.random.randint(0, 70, 12).reshape(4, 3)

print(f"Random scores array\n{a}\n")
print(f"cumlative sum of the above array\n{np.cumsum(a)}\n")
print(f"cumlative product of the above array\n{np.cumprod(a)}\n")

print(f"Random scores array\n{b}\n")
print(f"Cumlative sum of the 2D array\n{np.cumsum(b,axis=1)}\n")
print(f"Cumlative product of the 2D array\n{np.cumprod(b,axis=1)}\n")

# Percentile : compute nth Percentile of a given data along specified axis

print(f"Random scores array\n{a}\n")
print(f"100th Percentile value: {np.percentile(a,100)}\n")
print(f"50th percentile value: {np.percentile(a,50)}\n")
print(np.median(a))
