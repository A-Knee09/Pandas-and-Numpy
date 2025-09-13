import pandas as pd

# Creating series of csv having one col

"""
By defualt it will be a datafram , on making squeeze columns it converts to series
squeeze(True) , squeeze("columns") and squeeze() , all work
"""

subs_csv = pd.read_csv("./csv/subs.csv").squeeze(True)
print(f"{subs_csv}\n")
print(f"Type : {type(subs_csv)}\n")


# CSV with 2 col

# index_col = defines which column should be the index
kholi_csv = pd.read_csv("./csv/kohli_ipl.csv", index_col="match_no").squeeze(True)
print(f"{kholi_csv}\n")

movies = pd.read_csv("./csv/bollywood.csv", index_col="movie").squeeze(True)
print(f"{movies}\n")
