import pandas as pd

# sort_values : Sorts the values

vk = pd.read_csv("./csv/kohli_ipl.csv", index_col="match_no").squeeze()
# Print only the value from the top row
print(f"{vk.sort_values(ascending=False).head(1).values[0]}\n")

# vk.sort_values(inplace=True), Sorts the value but makes permanent changes to the series

movies = pd.read_csv("./csv/bollywood.csv", index_col="movie").squeeze()
print(f"{movies.sort_index()}\n")
