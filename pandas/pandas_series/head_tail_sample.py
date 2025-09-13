import pandas as pd

sep = 30 * "-"

# head : Returns first five rows by default otherwise custom count can be done

movies = pd.read_csv("./csv/bollywood.csv", index_col="movie").squeeze(True)
print(f"{movies}\n")

print(f"First five movies\n{sep}\n{movies.head()}\n")
print(f"First eight movies\n{sep}\n{movies.head(8)}\n")

# tail : same as head but gives the last n rows
print(f"Last five movies\n{sep}\n{movies.tail()}\n")
print(f"Last ten movies\n{sep}\n{movies.tail(10)}\n")

# Sample: Random values are selected as a sample
print(f"Sample Data with 10 random values\n{sep}\n{movies.sample(10)}")
