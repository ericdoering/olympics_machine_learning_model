import os
import pandas as pd

if os.path.isfile("teams.csv") and os.access("teams.csv", os.R_OK):
    columns_to_keep = ["team", "country", "year", "athletes", "age", "prev_medals", "medals"]
    teams = pd.read_csv("teams.csv")
    teams = teams[columns_to_keep]
    print(teams.head(10))
else:
    print("Error: 'teams.csv' does not exist or is not readable.")