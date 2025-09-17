"""
A dataframe is a rectangular data (rows and columns) , 1 row or 1 column is a series
"""

import pandas as pd

# dataframe using lists

student_data = [[120, 80, 10], [110, 70, 7], [130, 100, 14], [90, 50, 4]]

students = pd.DataFrame(student_data, columns=["IQ", "Marks", "Package (LPA)"])
print(f"{students}\n")

students_dict = {
    "IQ": [120, 110, 130, 90],
    "Marks": [80, 70, 100, 50],
    "Package (LPA)": [10, 7, 14, 4],
}

students = pd.DataFrame(students_dict)
print(f"{students}\n")

# Using CSV since we won't be the one creating dicts and list irl
movies = pd.read_csv("./csv/movies.csv")
print(f"{movies}\n")

ipl = pd.read_csv("./csv/ipl-matches.csv")
print(f"{ipl}\n")
