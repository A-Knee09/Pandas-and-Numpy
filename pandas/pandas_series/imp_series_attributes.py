import pandas as pd
import numpy as np
import sys

movies = pd.read_csv("./csv/bollywood.csv", index_col="movie").squeeze(True)
ipl = pd.read_csv("./csv/kohli_ipl.csv", index_col="match_no").squeeze(True)
subs = pd.read_csv("./csv/subs.csv").squeeze()
# astype : Change the data astype

print(f"Memory using int64: {sys.getsizeof(ipl)}\n")

print(f"Memory using int32: {sys.getsizeof(ipl.astype('int32'))}")

print(f"{ipl}\n")

# between : get values between a range
print(f"Matches where 51<runs<99\n{ipl[ipl.between(51,99)]}\n")
print(f"Number of matches where 51<runs<99 : {ipl[ipl.between(51,99)].size}\n")

# clip : Same as numpy clip , values are set between the range ex. get values between 10,20, values lower than 10 are replaced with 10 and more than 20 are set to 20
print(f"{subs}\n")
print(f"After Clipping(100,200)\n{subs.clip(100,200)}\n")

# drop_duplicates : drops duplicate values

temp = pd.Series([1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6])
print(f"{temp}\n")
print(f"{temp.drop_duplicates()}\n")
print(
    f"{temp.drop_duplicates(keep='last')}\n"
)  # Drop all the duplicates except last. By default first

# Duplicated: Returns boolean true and false if a value is Duplicated
print(f"{temp.duplicated()}")
print(f"Number of duplicated values: {temp.duplicated().sum()}\n")

# isnull: Returns boolean, if a value is null then True. Better used with sum

temp = pd.Series([1, 2, np.nan, 4, 5, np.nan, np.nan, 8])
print(f"{temp}\n")
print(f"Number of null values: {temp.isnull().sum()}\n")

# dropna : removes the nan values
print(f"{temp.dropna()}\n")

# fillna : replaces the null values with another given value
print(f"Null values replaced with 0\n{temp.fillna(0)}")
print(f"Null values replaced with Mean of dataset\n{temp.fillna(temp.mean())}\n")

# isin: returns boolean, finds out whehter a value is in a dataset
print(f"Matches where Virat kohli got out at 49 and 99\n{ipl[ipl.isin([49,99])]}\n")

# apply: Lets you apply your own function
print(
    movies.apply(lambda x: x.split()[0].upper())
)  # Prints the first name of actor in upper case

# copy: Creates a seperate copy, doesnt make changes to the orignal one

print(f"\n{ipl}\n")
vk = ipl.head().copy()
print(f"{vk}\n")
vk[1] = 100
print(f"{vk}\n")
print(f"{ipl}\n")
