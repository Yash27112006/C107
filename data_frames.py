import pandas as pd
import csv

filter_df = pd.read_csv('data.csv')
filtered = filter_df.filter(["level", "attempt"])
regex_filter = filter_df.filter(regex = '[tT]')
print(regex_filter)


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

# print(df)
# print(df.loc[0:2])
# print(df.loc[[0,2]])

