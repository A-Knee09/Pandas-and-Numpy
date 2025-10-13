import pandas as pd

bt = pd.read_csv("./csv/batsman_runs_ipl.csv")
print(f"{bt.head()}\n")


bt["batsmen_rank"] = bt["batsman_run"].rank(ascending=False)
print(f"{bt.sort_values('batsmen_rank')}\n")
