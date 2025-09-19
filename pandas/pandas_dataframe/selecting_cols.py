import pandas as pd

ipl = pd.read_csv("./csv/ipl-matches.csv")
movies = pd.read_csv("./csv/movies.csv")

print(f"{movies}\n")

# Selecting one col (series) -> movies['col_name']

print(f"{movies['title_x']}\n")
print(f"{ipl['Venue']}\n")
print(f"{type(ipl['Venue'])}\n")

# Selecting multiple cols using fancy indexing, columns are printed the same pattern in which they are passed as arguement. If I pass 'title_x' after 'actors' it will print title at last

print(f"{movies[['title_x','year_of_release','actors']]}")
print(f"{type(movies[['title_x','year_of_release','actors']])}\n")

# Printing the teams and who won
print(f"{ipl[['Team1','Team2','WinningTeam']]}\n")
