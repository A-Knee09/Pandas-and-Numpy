import numpy as np

image_grid = np.random.randint(0, 255, size=(100, 100))

print(f"Image Grid\n\n{image_grid}\n")

padded = np.pad(image_grid, pad_width=1, mode="edge")

blurred = (
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
