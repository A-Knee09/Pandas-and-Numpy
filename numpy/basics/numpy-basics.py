import numpy as np

SEP = "-" * 30


def section(title):
    """Prints a formatted section title."""
    print(f"\n{SEP} | {title} | {SEP}\n")


def explain(text):
    """Prints an explanation with proper spacing."""
    print(text.strip() + "\n")


# -------------------------------
# Array Dimensions
# -------------------------------
section("ARRAY DIMENSIONS")

arr_one_dim = np.array([1, 2, 3])
print("One Dimensional Array (Vector):\n", arr_one_dim, "\n")

arr_two_dim = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Two Dimensional Array (Matrix):\n", arr_two_dim, "\n")

arr_three_dim = np.array([[[1, 2], [3, 4], [5, 6]]])
print("Three Dimensional Array (Tensor):\n", arr_three_dim, "\n")

# -------------------------------
# Data Types
# -------------------------------
section("DTYPES")

print("Float Dtype:", np.array([1, 2, 3], dtype="float"))
print("Bool Dtype:", np.array([1, 2, 3], dtype="bool"))
print("Complex Dtype:", np.array([1, 2, 3], dtype="complex"), "\n")

# -------------------------------
# arange and reshape
# -------------------------------
section("arange and reshape")

explain(
    """arange is used for creating a range of numbers and works like Python's range().
reshape changes the array's shape to (rows, columns).
The product of rows × columns must equal the total number of elements.
"""
)

print("Range of numbers from 0-10 with step 2:\n", np.arange(0, 11, 2), "\n")
print("Matrix with 4 rows and 3 columns:\n", np.arange(1, 13).reshape(4, 3), "\n")

# -------------------------------
# Ones, Zeros, Random
# -------------------------------
section("Ones, Zeros and Random")

explain(
    """np.ones and np.zeros create an (n × m) matrix of ones or zeros.
np.random.random generates random values between 0 and 1 for a given shape.
"""
)

print("3×4 matrix of ones:\n", np.ones((3, 4)), "\n")
print("3×4 matrix of zeros:\n", np.zeros((3, 4)), "\n")
print("3×4 matrix of random numbers:\n", np.random.random((3, 4)), "\n")

# -------------------------------
# Linspace
# -------------------------------
section("linspace")

explain(
    """numpy.linspace(start, stop, num)
Returns evenly spaced numbers over a given range.

- start → first number in the range
- stop → last number in the range
- num → number of evenly spaced values (default = 50)

Unlike np.arange (which uses a step size), linspace ensures equal spacing 
between values even if the step is unknown.
"""
)

print("Linspace from 0 to 1 with 5 values:\n", np.linspace(0, 1, 5), "\n")

# -------------------------------
# Identity Matrix
# -------------------------------
section("Identity Matrix")

explain(
    """numpy.identity creates a square matrix with 1's along the diagonal 
and 0's elsewhere. Takes one argument for both rows and columns.
"""
)

print("3×3 Identity matrix:\n", np.identity(3), "\n")
