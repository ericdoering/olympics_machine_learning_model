import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

if os.path.isfile("teams.csv") and os.access("teams.csv", os.R_OK):
    columns_to_keep = ["team", "country", "year", "athletes", "age", "prev_medals", "medals"]
    teams = pd.read_csv("teams.csv")
    teams = teams[columns_to_keep]
    teams = teams.dropna()
    # print(teams.head(10))
    # sns.lmplot(x='athletes', y='medals', data=teams, fit_reg=True, ci=None)
    # sns.lmplot(x='age', y='medals', data=teams, fit_reg=True, ci=None)
    # teams.plot.hist(y="medals")
    # plt.show()
else:
    print("Error: 'teams.csv' does not exist or is not readable.")
