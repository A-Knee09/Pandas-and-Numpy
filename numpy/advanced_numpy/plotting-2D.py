import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("TkAgg")

# x = y , eq for straight line through origin
x = np.linspace(-10, 10, 100)
y = x

plt.plot(x, y)
plt.show()

# y = x^2 , parabola
x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)
plt.show()

# y = sin(x)

x = np.linspace(-10, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()

# sigmoid

x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))

plt.plot(x, y)
plt.show()
