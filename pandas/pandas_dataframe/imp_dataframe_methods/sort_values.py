import pandas as pd

movies = pd.read_csv("./csv/movies.csv")
print(f"{movies.sort_values('title_x')}")
print(f"{movies.sort_values(['year_of_release','title_x'])}")

# Keep year of release ascending and title to be descending
print(f"{movies.sort_values(['year_of_release','title_x'], ascending=[True,False])}")
