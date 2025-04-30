import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


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

    test.loc[test["predictions"] < 0, "predictions"] = 0
    test["predictions"] = test["predictions"].round()

    error = mean_absolute_error(test["medals"], test["predictions"])
    errors = (test["medals"] - test["predictions"]).abs()
    error_by_team = errors.groupby(test["team"]).mean()

    medals_by_team = test["medals"].groupby(test["team"]).mean()
    error_ratio = error_by_team / medals_by_team
    error_ratio = error_ratio[~pd.isnull(error_ratio)]
    error_ratio = error_ratio[np.isfinite(error_ratio)]

    error_ratio.plot.hist()

    print(error_ratio)

    # teams.plot.hist(y="medals")
    plt.show()
else:
    print("Error: 'teams.csv' does not exist or is not readable.")
