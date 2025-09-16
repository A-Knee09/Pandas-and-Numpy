"""
Writing on real world data is not done often neither is recommended, but pandas still provides an option
"""

import pandas as pd

marks = {"Maths": 67, "English": 80, "Science": 89, "Hindi": 100}
marks_series = pd.Series(marks, name="Anirudh's Marks")

print(f"Marks\n{marks_series}\n")

# Using index
marks_series[1] = 100
print(f"Marks\n{marks_series}\n")

# If index doesnt not exist it will create one. This would give an error while reading but not while writing
marks_series["evs"] = 92
print(f"Marks\n{marks_series}\n")

# Slicing also works

# fancy indexing also works
marks_series[[0, 1, 3]] = [50, 50, 50]
print(f"Marks\n{marks_series}\n")

# You can use labels as well
