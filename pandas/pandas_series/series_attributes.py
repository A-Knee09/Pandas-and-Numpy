import pandas as pd

marks = {"Maths": 78, "Science": 82, "Hindi": 70, "Computer Science": 96, "English": 88}

marks_series = pd.Series(marks, name="Anirudh's Marks")

print(f"{marks_series}\n")

# size : Returns number of items in a series
print(f"Number of items in the series : {marks_series.size}\n")

# dtype : Returns data type
print(f"Data type of the series : {marks_series.dtype}\n")

# name : Name of the series
print(f"Name of the series : {marks_series.name}\n")

# is_unique : True if every item is unique else false
print(f"{marks_series.is_unique}\n")

# index: Returns the index object
print(f"{marks_series.index}\n")

# values: Returns values in series
print(f"{marks_series.values}\n")
