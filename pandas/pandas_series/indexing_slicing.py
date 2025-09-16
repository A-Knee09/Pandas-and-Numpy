import pandas as pd

vk = pd.read_csv("./csv/kohli_ipl.csv", index_col="match_no").squeeze()
movies = pd.read_csv("./csv/bollywood.csv", index_col="movie").squeeze()

# indexing : Works the same as base python, both positive and negative

print(f"From index 10 to 20\n{vk[10:20]}\n")
print(f"Movie from last index\n{movies[-1]}\n")

# indexing using label
print(f"{movies['2 States (2014 film)']}\n")

# Fancy indexing also works
print(f"Movies at index 1,4,5,6\n{movies[[1,4,5,6]]}\n")
