import numpy as np

# 1. Generate dataset
sensor_readings_celsius = np.random.randint(18, 45, 100).reshape(10, 10)
print("Sensor Readings (°C):\n", sensor_readings_celsius, "\n")

# 2. Anomalous values (<20 or >40)
mask = (sensor_readings_celsius < 20) | (sensor_readings_celsius > 40)
anomalous_readings = sensor_readings_celsius[mask]
print("Anomalous Readings:\n", anomalous_readings, "\n")

# 3. Normalization (min-max)
arr = sensor_readings_celsius
normalized = (arr - arr.min()) / (arr.max() - arr.min())
print("Normalized Array:\n", normalized, "\n")

# 4. Row-wise & column-wise stats
row_means = arr.mean(axis=1)
col_max = arr.max(axis=0)
row_var = arr.var(axis=1)

print("Row-wise Mean:\n", row_means, "\n")
print("Column-wise Max:\n", col_max, "\n")
print("Row Variance:\n", row_var, "\n")
print("Row with Highest Variance:", row_var.argmax(), "\n")

# 5. 3×3 Smoothing Filter
padded = np.pad(arr, pad_width=1, mode="edge")

smooth = (
    padded[0:-2, 0:-2]
    + padded[0:-2, 1:-1]
    + padded[0:-2, 2:]
    + padded[1:-1, 0:-2]
    + padded[1:-1, 1:-1]
    + padded[1:-1, 2:]
    + padded[2:, 0:-2]
    + padded[2:, 1:-1]
    + padded[2:, 2:]
) / 9

print("Smoothed Array (3×3 filter):\n", smooth)
