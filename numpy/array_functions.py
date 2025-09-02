import numpy as np

a1 = np.random.random((3, 3))
a1 = np.round(a1 * 100)
print(f"A1:\n{a1}\n")

# max,min,sum,prod : As the name suggests, finds out max/min in the matrix, sums/multiplies the element of matrix
# axis -> 0: column, 1: row, works with all the methods above
print(f"Max : {np.max(a1)}")
print(f"Max of from each rows : {np.max(a1, axis=1)}")

print(f"Min: {np.min(a1)}")
print(f"Min from each column: {np.min(a1, axis=0)}")

print(f"Sum of all elements : {np.sum(a1)}")
print(f"Product of all elements : {np.prod(a1)}\n")

# mean, median, std, var
# axis is applicable to them as well

print(f"Mean: {np.mean(a1)}")
print(f"Mean of each row: {np.mean(a1, axis= 1)}")

print(f"Median: {np.median(a1)}")
print(f"Median of each row: {np.median(a1, axis= 1)}")

print(f"Standard deviation: {np.std(a1)}")
print(f"Variance: {np.var(a1)}\n")

# Dot product : Pretty imp, calculates the dot product of two matrix, condition: matrix1 col = matrix2 row

a2 = np.arange(12).reshape(3, 4)
a3 = np.arange(12, 24).reshape(4, 3)

print(f"A2 :\n{a2}")
print(f"A3 :\n{a3}\n")

print(f"Dot product of A2 and A3:\n{np.dot(a2,a3)}\n")

# Log and exponents of each item
print(f"Log of A1:\n{np.log(a1)}")
print(f"Exponent of A1:\n{np.exp(a1)}\n")

# round,floor,ceil

a4 = np.random.random((2, 3))
print(f"A4:\n{a4}\n")

print(f"Rounded values of A4:\n{np.round(a4)}\n")
print(f"Floored values of A4:\n{np.floor(a4)}\n")
print(f"Ceil values of A4:\n{np.ceil(a4)}\n")
