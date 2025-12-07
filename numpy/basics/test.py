import numpy as np

m = np.zeros((8, 8), dtype=int)
# m[[0, -1], :] = 1
# m[:, [0, -1]] = 1
# print(m)

# m[1::2, ::2] = 1
# m[::2, 1::2] = 1
# print(f"{m}\n")
#
# x = np.arange(1, 13)
# # x.resize(5, 5)
# y = np.resize(x, (6, 6))
# # print(f"{x}\n")
# print(f"{y}\n")

# x = np.arange(1, 10).reshape(3, 3)
# print(f"{x}\n")
#
# for row in x:
#     for element in row:
#         print(element)

x = np.arange(1, 10).reshape(3, 3)
y = np.insert(x, 2, [0, 0, 0], axis=1)
print(x)
print(y)

l = np.array(["PHP Exercises", "Practice", "Solution"])
l = np.char.startswith(l, "P")
print(l)

s = np.array([3, 6, 1, 8, 9, 4, 1])
g = np.where(s % 2 == 0, "even", "odd")
print(g)
