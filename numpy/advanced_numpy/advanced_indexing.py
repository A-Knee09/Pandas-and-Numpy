import numpy as np

a = np.arange(24).reshape(6, 4)

print(f"Matrix A\n{a}\n")

# Lets say I want to fetch rows 1,3 and 4. There is no pattern here so slicing or steps won't work
# In fancy indexing you provide a list with whatever that needs to be fetched

print(f"First,Third and Last row\n{a[[0, 2, 3]]}\n")

print(f"First third and last column\n{a[:,[0,2,3]]}\n")

# Boolean Indexing
# 24 random numbers between 1,100
b = np.random.randint(1, 100, 24).reshape(6, 4)
print(f"Matrix B\n{b}\n")


# b>50 will return a boolean matrix where elements greater than 50 are printed as true. We can use this boolean matrix as a mask for printing only the numbers greater than 50
print(f"All the numbers greater than 50 in matrix B\n{b[b>50]}\n")

print(f"All even items in matrix B\n{b[b%2==0]}\n")

# Since we're operating with boolean values we use bitwise &. We don't use logical and
print(f"All numbers greater than 50 and even\n{b[(b>50) & (b%2==0)]}\n")

# We can also use != sign or ~
print(f"All numbers which are not divisible by 7\n{b[~(b%7==0)]}\n")
