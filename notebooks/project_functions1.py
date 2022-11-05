import pandas as pd
import numpy as np
def load_and_process(path):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv(path)
        .loc[lambda x: x['Global_Sales'] >= 0]
        .loc[lambda x: x['NA_Sales'] >= 0]
        .loc[lambda x: x['JP_Sales'] >= 0]
        .loc[lambda x: x['EU_Sales'] >= 0]
        .loc[lambda x: x['Other_Sales'] >= 0]
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .drop(['User_Count','Critic_Count', 'Rating','User_Score'], axis=1)
          .dropna(axis=0)
      )

    # Make sure to return the latest dataframe

    return df2 