import pandas as pd

students_dict = {
    "Name": ["Anirudh", "Anamika", "Asmi", "Palak", "Tanvi", "Ashish"],
    "IQ": [135, 120, 125, 130, 110, 140],
    "Marks": [70, 90, 88, 75, 68, 100],
    "Package": [10, 7, 9, 12, 6, 14],
}

movies = pd.read_csv("./csv/movies.csv")
ipl = pd.read_csv("./csv/ipl-matches.csv")

students = pd.DataFrame(students_dict)
# Sets a column as index
students.set_index("Name", inplace=True)

# iloc : searches using index positions
# loc : searches using index labels, iloc still works even with label indexes

print(f"{movies.iloc[0]}\n")  # First movies/row. This is also a series
print(f"{type(movies.iloc[0])}\n")

# slicing
print(f"{movies.iloc[0:5]}\n")
print(f"{movies.iloc[5:16:2]}\n")

# fancy indexing
print(f"{movies.iloc[[0,4,5]]}\n")

print(f"{students}\n")
print(f"{students.loc['Anirudh']}\n")

# slicing works but it also includes the last element mentioned
print(f"{students.loc['Anirudh':'Palak']}\n")
print(f"{students.loc['Anirudh':'Tanvi':2]}\n")

# Fancy indexing
print(f"{students.loc[['Anirudh' , 'Anamika', 'Ashish']]}\n")

# Selecting both rows and columns
print(f"{movies.loc[0:2,'title_x':'poster_path']}\n")
print(f"{movies.loc[0:4 , ['title_x','imdb_id','actors','release_date']]}\n")
