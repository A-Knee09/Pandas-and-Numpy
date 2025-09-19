import pandas as pd

students_dict = {
    "IQ": [120, 110, 130, 90],
    "Marks": [80, 70, 100, 50],
    "Package (LPA)": [10, 7, 14, 4],
}
ipl = pd.read_csv("./csv/ipl-matches.csv")
movies = pd.read_csv("./csv/movies.csv")
students = pd.DataFrame(students_dict)

# sum() : Sums up columns, if its a string it concats them, has an axis arguement -> 1 for row 0 for col
print(f"{students.sum()}\n")

# mean() : axis arguement
print(f"{students.mean(axis=1)}\n")

# var() : axis arguement
print(f"{students.var(axis=0)}\n")
