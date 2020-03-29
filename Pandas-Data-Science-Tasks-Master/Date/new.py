import pandas as pd

df = pd.read_csv('pokemon_data.csv')
df.nrows
#print(df.iloc[0:4])
#for index, row in df.iterrows():
#print(df.iloc[2,1])
  #print(index, row['Name'])
df.loc[df['Type 1'] == "Grass"]

print(df)
