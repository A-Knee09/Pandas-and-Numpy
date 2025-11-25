# 1. NumPy Assignment — “Sensor Grid Analysis”

You’re given data from a 10×10 grid of sensors deployed in a warehouse.
Each sensor measures temperature every hour. You receive one hour of readings as a NumPy array.

## Your Tasks

---

### 1. Generate the dataset

Create a 10×10 NumPy array of floats with simulated temperature values between 18°C and 45°C.

### 2. Detect anomalies

Any value > 40°C or < 20°C is an anomaly.
Produce a boolean mask AND a separate array of all anomalous readings.

### 3. Normalize the grid

Apply min–max normalization on the full grid (new range: 0–1).
Do it manually using NumPy ops, no loops.

### 4. Compute row-wise and column-wise stats

Mean temperature per row

Max temperature per column

Which row has the highest variance?

Spatial smoothing (important real-world skill)
Apply a 3×3 averaging filter on the array to simulate noise reduction.
Use slicing and vectorized operations — no for-loops.

Bonus (realistic)
Visualize the grid using matplotlib.imshow (if you want tightened skills).

This tests: indexing, masking, filtering, vectorization, broadcasting, reductions, and thinking like a data person.
