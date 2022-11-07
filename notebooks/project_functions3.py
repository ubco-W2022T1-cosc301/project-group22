import pandas as pd
import numpy as np

def load_and_process(path):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv(path)
        .dropna(subset=['Global_Sales'])
        .loc[lambda x: x['Year_of_Release'] <= 2016]
        .loc[lambda x: x['Critic_Score'] >= 0]
        
    )
        
        # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .drop(['Developer','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Critic_Count'], axis=1)
      )

    # Make sure to return the latest dataframe

    return df2 