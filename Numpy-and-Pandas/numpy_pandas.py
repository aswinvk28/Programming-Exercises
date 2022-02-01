import matplotlib.pyplot as plt
import pandas as pd

def print_rows(df):
  print("First 5 rows: ", df.head(5))
  print("Last 5 rows: ", df.tail(5))
  
def highest_paid(df):
  return df.loc[df['salary'].rank(method='max').index[0]]

def average_salary(df):
  return df.salary.mean()

def plot_salaries(df):
  fig, ax = plt.subplots(1,1, figsize=(12,8))
  df.salary[df.sex == 'Male'].hist(ax=ax)
  df.salary[df.sex == 'Female'].hist(ax=ax)
  ax.legend()
  ax.set(xlabel="Salary", ylabel="Count")
  fig.show()
  input("exit: ")
  
if __name__ == "__main__":
  
  df = pd.read_csv("Salaries.csv")
  print_rows(df)
  print(highest_paid(df))
  print(average_salary(df))
  plot_salaries(df)