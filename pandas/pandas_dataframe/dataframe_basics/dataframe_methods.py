import pandas as pd

students_dict = {
    "IQ": [120, 110, 130, 90],
    "Marks": [80, 70, 100, 50],
    "Package (LPA)": [10, 7, 14, 4],
}

movies = pd.read_csv("./csv/movies.csv")
ipl = pd.read_csv("./csv/ipl-matches.csv")
students = pd.DataFrame(students_dict)

# head(n) : Returns the first/top n values. By default 5 if n not given
print(f"First two movies in Movies DataFrame\n{movies.head(2)}\n")

# tail(n) : Returns the last/bottom n values. By default 5 if n not given
print(f"Last two IPL matches in IPL DataFrame\n{ipl.tail(2)}\n")

# smaple(n) : Returns random n values from the dataframe
print(f"Sample of 5 from IPL dataframe\n{ipl.sample(5)}\n")

# info() : Returns some info/summary about the dataframe. Columns, number of not null values, Dtype and dtypes, memory usage,...
print(f"Info/Summary of movies dataframe\n{movies.info()}\n")

# describe() : Provides summary statistics for numerical columns in a DataFrame. Focuses on characteristics and statistical properties
print(f"Statistical Properties of movies\n{movies.describe()}\n")

# isnull() : Returns true/false if value null or not
print(f"Movies is Null\n{movies.isnull()}\n")
print(f"How many null in Movies\n{movies.isnull().sum()}\n")

# duplicated() : Tells if there is duplicated data in DataFrame. Index -> True/False. True means row has been duplicated
print(f"Movies duplicated\n{movies.duplicated()}\n")
print(f"How many movies duplicated: {movies.duplicated().sum()}\n")

# rename() : Renames columns , df.rename(columns={'orignal_col':'renamed_col'}) , not permanent change but can be done using inplace = true parameter
print(f"Orignal Students DataFrame\n{students}\n")
print(
    f"New Students DataFrame\n{students.rename(columns={'Marks':'Precentage' , 'Package (LPA)':'LPA'})}\n"
)
