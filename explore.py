import pandas as pd
import functions
import numpy as np


# races = pd.read_csv('./data/races.csv')



# def explore(csv):
#     df = pd.read_csv(csv, na_values="\\N")
#     print(df.shape)
#     print(df.describe())
#     print(df.dtypes)
#     return df


# explore('./project1/data/circuits.csv')


config = functions.import_config('./project1/config.json')

results = functions.import_csv('./project1/data/lap_times.csv')
df1 = functions.replace_str(results, config["nullable_columns"], '\\N', np.nan)
# df2 = functions.drop_columns(df1, config['drop_columns'])
# #print(df2['time'].to_string())
# df3 = functions.datatype_col(df2, config["columns_datatypes"])
print(df1.dtypes)