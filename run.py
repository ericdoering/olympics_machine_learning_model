import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if os.path.isfile("teams.csv") and os.access("teams.csv", os.R_OK):
    columns_to_keep = ["team", "country", "year", "athletes", "age", "prev_medals", "medals"]
    teams = pd.read_csv("teams.csv")
    teams = teams[columns_to_keep]
    teams = teams.dropna()
    # print(teams.head(10))
    # sns.lmplot(x='athletes', y='medals', data=teams, fit_reg=True, ci=None)
    # sns.lmplot(x='age', y='medals', data=teams, fit_reg=True, ci=None)
    reg = LinearRegression()
    
    train = teams[teams["year"] < 2012].copy()
    test = teams[teams["year"] >= 2012].copy()

    predictors = ["athletes", "prev_medals"]
    target = "medals"

    reg.fit(train[predictors], train[target])
    predictions = reg.predict(test[predictors])
    test["predictions"] = predictions

    print(predictions[0:20])

    # teams.plot.hist(y="medals")
    # plt.show()
else:
    print("Error: 'teams.csv' does not exist or is not readable.")
