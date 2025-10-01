import pandas as pd

students_dict = {
    "IQ": [120, 110, 130, 90],
    "Marks": [80, 70, 100, 50],
    "Package (LPA)": [10, 7, 14, 4],
}

movies = pd.read_csv("./csv/movies.csv")
ipl = pd.read_csv("./csv/ipl-matches.csv")
students = pd.DataFrame(students_dict)

# Shape : Number  of rows and colums, Is used oftenly
print(f"Number of rows and colums in movies csv: {movies.shape}\n")
print(f"Number of rows and colums in IPL csv: {ipl.shape}\n")

# dtypes : Data type of each series
print(f"Data type of each column in Movies csv\n{movies.dtypes}\n")
print(f"Data type of each column in IPL csv\n{ipl.dtypes}\n")

# index : Returns the range of indexs
print(f"Range index of movies csv: {movies.index}\n")

# colums : Fetches all the colums
print(f"All the columns in IPL csv\n{ipl.columns}\n")

# values: Fetches all the values, Returns a numpy array
print(f"Values in Student DataFrame\n{students.values}\n")
print(f"Values in IPL DataFrame\n{ipl.values}\n")
