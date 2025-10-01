import pandas as pd

ipl = pd.read_csv("./csv/ipl-matches.csv")

ipl.info()

# astype : Change one datatype to another, helps with optimization

ipl["ID"] = ipl["ID"].astype("int32")
ipl["Season"] = ipl["Season"].astype("category")
ipl["Team1"] = ipl["Team1"].astype("category")
ipl["Team2"] = ipl["Team2"].astype("category")
ipl["WinningTeam"] = ipl["WinningTeam"].astype("category")
ipl["Venue"] = ipl["Venue"].astype("category")
ipl["Umpire1"] = ipl["Umpire1"].astype("category")
ipl["Umpire2"] = ipl["Umpire2"].astype("category")
ipl["City"] = ipl["City"].astype("category")

print("IPL info after converting dataypes to optimized ones\n")
ipl.info()
