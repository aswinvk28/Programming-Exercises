import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def pokemon_type(df):
  return df.groupby('Type')['Total'].agg('sum')

def powerful_pokemon(df):
  df['Power_Total'] = df.HP / df.Total
  df.groupby('Type')['Power_Total'].agg('sum')
  
def plot_pokemon(df):
  print(df.mean())
  print(df.var())
  plt.subplot(1,2,1)
  df.mean().plot(kind='bar')
  plt.subplot(1,2,2)
  df.var().plot(kind='bar')
  plt.show()

if __name__ == "__main__":
  
  df = pd.read_csv("all_pokemon.csv")
  print(pokemon_type(df))
  print(powerful_pokemon(df))
  plot_pokemon(df)
  input("exit:")
