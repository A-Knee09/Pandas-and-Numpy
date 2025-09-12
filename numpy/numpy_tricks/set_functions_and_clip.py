import numpy as np

a = np.arange(1, 6)
b = np.arange(3, 8)

print(f"Array A\n{a}\n")
print(f"Array A\n{b}\n")

print(f"Union\n{np.union1d(a,b)}\n")
print(f"intersection\n{np.intersect1d(a,b)}\n")
print(f"Difference [A-B]\n{np.setdiff1d(a,b)}\n")
print(f"Difference [B-A]\n{np.setdiff1d(b,a)}\n")
print(f"XOR\n{np.setxor1d(b,a)}\n")
print(f"Membership\n{np.in1d(a,10)}\n")

# Clip : limit the values in an array

c = np.random.randint(1, 100, 20)
print(f"C matrix\n{c}\n")

print(
    f"{np.clip(c, a_min=25, a_max=75)}"
)  # Values lower than 25 will be replaced by 25 and values higher than 75 will be replaced by 75
