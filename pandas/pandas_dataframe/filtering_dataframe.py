import pandas as pd

movies = pd.read_csv("./csv/movies.csv")
ipl = pd.read_csv("./csv/ipl-matches.csv")

# print(f"{ipl.head(2)}\n")
# print(f"{movies.head(2)}\n")

# Find all the final winners

"""
The csv has a column called match number.
From this column we extract all the matches having match number as final
The above would return a boolean series which we can use as a mask for boolean indexing
We then use the new table and extract the season and the winning team
"""

mask = ipl["MatchNumber"] == "Final"
print(f"{mask}\n")

finals_ipl_df = ipl[mask]
print(f"Teams qualified for Finals\n{finals_ipl_df}\n")

print("Winning Teams and their Seasons\n")
print(f"{finals_ipl_df[['Season','WinningTeam']]}\n")

# All this could be done in a single line as well : ipl[ipl['MatchNumber'] == 'Final'][['Season','WinningTeam']]

# How many super over finishes have occured

"""
Basically finding out the matches where super over occured and then the number of rows will provide the answer
"""

print(
    f"Number of matches where superover have happened: {ipl[ipl['SuperOver'] == 'Y'].shape[0]}\n"
)

# How many matches csk won in kolkata

csk_wins = ipl[
    (ipl["City"] == "Kolkata") & (ipl["WinningTeam"] == "Chennai Super Kings")
].shape[0]
print(f"Number of matches CSK won in Kolkata : {csk_wins}\n")

# Toss winner is the match winner in percentage. Does winning the toss do anything

wins = (ipl[ipl["TossWinner"] == ipl["WinningTeam"]].shape[0] / ipl.shape[0]) * 100
print(f"{wins} % of the teams won the toss and the match as well\n")

# Movies with rating higher than 8 and votes>10000
ratings = movies[(movies["imdb_rating"] > 8) & (movies["imdb_votes"] > 10000)]
print(f"{ratings[['title_x','imdb_rating','imdb_votes']]}")
print(f"Number of movies with imdb votes > 10000 and 8+ ratings : {ratings.shape[0]}")
