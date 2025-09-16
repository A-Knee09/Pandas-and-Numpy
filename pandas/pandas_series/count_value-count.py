import pandas as pd

movies = pd.read_csv("./csv/bollywood.csv", index_col="movie").squeeze(True)
print(f"{movies}\n")


# value_counts: used to count the occurrences of unique values in a Series or DataFrame colum. For ex how many movies has an actor done

print(f"{movies.value_counts()}\n")

# count : Total number of items present inside a series

print(f"{movies.count()}\n")
