import pandas as pd

vk = pd.read_csv("./csv/kohli_ipl.csv", index_col="match_no").squeeze()
movies = pd.read_csv("./csv/bollywood.csv", index_col="movie").squeeze()


print(f"{vk.sum()}\n")
print(f"{vk.prod()}\n")
print(f"Mean of vk\n{vk.mean()}\n")
print(f"Median of vk\n{vk.median()}\n")
print(f"Mode of vk\n{vk.mode()}\n")
print(f"Min\n{vk.min()}\n")
print(f"Max\n{vk.max()}\n")

# Describe : Will do all the above
print(f"Describe Movies\n{movies.describe()}\n")
print(f"Describe Virat Kholi CSV\n{vk.describe()}\n")
