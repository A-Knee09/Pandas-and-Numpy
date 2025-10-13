import pandas as pd
import matplotlib


a = pd.Series([1, 1, 1, 2, 2, 3])
marks = pd.DataFrame(
    [[100, 80, 10], [90, 70, 7], [120, 100, 14], [80, 70, 14], [80, 70, 14]],
    columns=["IQ", "Marks", "Package (LPA)"],
)

ipl = pd.read_csv("./csv/ipl-matches.csv")

# Value count (Series and Dataframe) : Returns the frequency count, how many times a value is present
print(f"Series A: {a}\n")
print(f"{a.value_counts()}\n")

print(f"Dataframe marks\n{marks}\n")
print(f"{marks.value_counts()}\n")  # How many times a row has been repeated

ipl.info()

# Find out which player has won the player of the match in finals and qualifiers
print(f"{ipl['Player_of_Match'].head(5)}\n")
print(f"{ipl['MatchNumber'].head(5)}\n")
print(f"{~ipl['MatchNumber'].str.isdigit()}\n")
print(f"{ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts()}\n")

# Toss decision plot : How much percent is batting or bowling preffered

print(f"{ipl['TossDecision'].value_counts().plot(kind='pie')}")

# how many matches each team has played -> A team can be present in team 1 and team 2 as well

print(
    f"{(ipl["Team1"].value_counts() + ipl["Team2"].value_counts()).sort_values(ascending=False)}\n"
)
