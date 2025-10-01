import pandas as pd

a = pd.Series([1,1,1,2,2,3])
marks = pd.DataFrame([
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,70,14],
    [80,70,14]
],columns=["IQ","Marks","Package (LPA)"])

ipl = pd.read_csv("./csv/ipl-matches.csv")

# Value count (Series and Dataframe) : Returns the frequency count, how many times a value is present
print(f"Series A: {a}\n")
print(f"{a.value_counts()}\n")

print(f"Dataframe marks\n{marks}\n")
print(f"{marks.value_counts()}\n") # How many times a row has been repeated

ipl.info()

# Find out which player has won the player of the match in finals and qualifiers

