import numpy as np
import pandas as pd

# Series is like a column

# string
countries = ["India", "Pakistan", "USA", "China", "Nepal"]

# making an object of countries using series class, it returns the name of the country along with an index
# dtype:Object usually means a string most of the time

print(f"Countries\n{pd.Series(countries)}\n")

# Integer
runs = [10, 50, 35, 27, 67, 100]
print(f"Runs\n{pd.Series(runs)}\n")

# Custom index
marks = [67, 55, 78, 64, 87]
subjects = ["Maths", "Science", "English", "Hindi", "Computer Science"]
print(f"{pd.Series(marks , index=subjects)}\n")

# Setting a name
series_name = print(f"{pd.Series(marks , index=subjects, name='Anirudh Marks')}\n")
print(f"{series_name}\n")

# Series using dict

marks = {"Maths": 67, "Science": 55, "English": 78, "Hindi": 64, "Computer Science": 87}

print(f"{pd.Series(marks, name="Anirudh's Marks")}")
