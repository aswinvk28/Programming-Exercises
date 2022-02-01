# Programming Exercises

- Cows and Bulls

```python

import random
import math

def generate_n_digit_random_number(n_digits=4):
  number = 0
  for i in range(n_digits):
    if i == 0:
        random_digit = random.randint(1,9)
    else:
        random_digit = random.randint(0,9)
    number += random_digit * 10**(n_digits-i-1)
  
  return number

def guess_number(number):
  guess_number = input("Guess the four digit number: ")
  guess_string = str(guess_number)
  number_string = str(number)
  cows = 0
  bulls = 0
  print(guess_string, number_string)
  for i in range(len(guess_string)):
    guess_str = guess_string[i]
    if guess_string[i] == number_string[i]:
      cows += 1
    elif guess_str in number_string:
      bulls += 1
  return (cows, bulls, guess_number)

if __name__ == "__main__":
  
  while(True):
      number = generate_n_digit_random_number(4)
      result = guess_number(number)
      print("Cows: ", result[0], " Bulls: ", result[1], " Number: ", number)
      if number == int(result[2]):
            break
  
```

- Images

```python

import numpy as np
from imageio import imread, imsave
import matplotlib.pyplot as plt

cat = imread("cat.jpg")
monkey = imread("test.jpg")

if __name__ == "__main__":
  
  # crop the image
  cropped_cat = cat[75:300, 75:300]
  cropped_monkey = monkey[40:200, 40:200]
  imsave("cropped_cat.jpg", cropped_cat)
  imsave("cropped_monkey.jpg", cropped_monkey)
  
  # make images brighter
  darker_cat = cat * [0.8,0.8,0.8]
  darker_monkey = monkey * [0.8,0.8,0.8]
  
  # make images darker
  brighter_cat = cat * [1.3,1.3,1.3]
  brighter_monkey = monkey * [1.3,1.3,1.3]
  
  plt.subplot(1,2,1)
  plt.imshow(monkey)
  plt.subplot(1,2,2)
  plt.imshow(np.uint8(np.clip(brighter_monkey, 0.0, 255.0)))
  plt.show()
  
  imsave("brighter_monkey.jpg", np.uint8(np.clip(brighter_monkey, 0.0, 255.0)))
  
  plt.subplot(1,2,1)
  plt.imshow(cat)
  plt.subplot(1,2,2)
  plt.imshow(np.uint8(np.clip(brighter_cat, 0.0, 255.0)))
  plt.show()
  
  imsave("brighter_cat.jpg", np.uint8(np.clip(brighter_cat, 0.0, 255.0)))
  
  plt.subplot(1,2,1)
  plt.imshow(cat)
  plt.subplot(1,2,2)
  plt.imshow(np.uint8(np.clip(darker_cat, 0.0, 255.0)))
  plt.show()
  
  imsave("darker_cat.jpg", np.uint8(np.clip(darker_cat, 0.0, 255.0)))
  
  plt.subplot(1,2,1)
  plt.imshow(monkey)
  plt.subplot(1,2,2)
  plt.imshow(np.uint8(np.clip(darker_monkey, 0.0, 255.0)))
  plt.show()
  
  imsave("darker_monkey.jpg", np.uint8(np.clip(darker_monkey, 0.0, 255.0)))
  
  input("exit: ")

```

- Numpy and Pandas

```python

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

```

- Pokemon

```python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def pokemon_type(df):
  return df.groupby('Type')['Total'].agg('count')

def powerful_pokemon(df):
  return df.groupby('Type')['Total'].agg('sum').sort_values(ascending=False).to_frame().iloc[0, :]
  
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
  print("----------------------")
  print(powerful_pokemon(df))
  print("----------------------")
  plot_pokemon(df)
  print("----------------------")
  input("exit:")

```

- Remove Duplicates in a List

```python

def remove_duplicates(elements, method='sets'):
  if method == 'sets':
    return list(set(elements))
  elif method == 'loop':
    array = []
    for ii, e in enumerate(elements[1:]):
      if e not in array:
        array.append(e)
    return array
  
if __name__ == "__main__":
  
  elements = [1,2,8,5,3,5,2,5,1,6,9,8,7,3,4,7]
  print(remove_duplicates(elements, method='loop'))

```

- Rock Paper Scissors Game

```python

import random 

def win():
  return "Congratulations, You Win! Want to start a new game?"

def lose():
  return "You Lose! Want to start a new game?"

if __name__ == "__main__":
    
    while(True):
      print("""
            Enter r for Rock, 
                  s for Scissors, 
                  p for Paper
            """)
      player_1 = input("Player 1: ")
      player_type = input("Press c for computer to play or h for human to play:")

      if player_type == 'h':
        player_2 = input("Player 2:")
      else:
        player_2 = random.choice(['r', 's', 'p'])

      if player_1 == 'r' and player_2 == 's':
        print(win())
      elif player_1 == 'r' and player_2 == 'p':
        print(lose())
      elif player_1 == 'r' and player_2 == 'r':
        print("Draw! try again")

      if player_1 == 's' and player_2 == 'r':
        print(lose())
      elif player_1 == 's' and player_2 == 'p':
        print(win())
      elif player_1 == 's' and player_2 == 's':
        print("Draw! try again")

      if player_1 == 'p' and player_2 == 'r':
        print(win())
      elif player_1 == 'p' and player_2 == 's':
        print(lose())
      elif player_1 == 'p' and player_2 == 'p':
        print("Draw! try again")
  
```

- Tic Tac Toe

```python

import numpy as np

def draw_game_board(user_input=[2,1], player='o', previous=None):
  if previous:
    previous_lines = previous.split("\n")
    dashed_lines = previous_lines[0]
    result = [dashed_lines, previous_lines[1], dashed_lines, previous_lines[3], dashed_lines, 
              previous_lines[5], dashed_lines]
    array = result[user_input[0]*2 + 1]
    array = array[:(user_input[1]*4 + 2)] + player + array[(user_input[1]*4 + 2):]
    result[user_input[0]*2 + 1] = array
  else:
      dashed_lines = """ --- --- --- """
      entries = """|   |   |   |"""
      result = [dashed_lines, entries, dashed_lines, entries, dashed_lines, entries, dashed_lines]
      array = result[user_input[0]*2 + 1]
      array = array[:(user_input[1]*4 + 2)] + player + array[(user_input[1]*4 + 2):]
      result[user_input[0]*2 + 1] = array
  return "\n".join(result)

game = np.zeros((3,3))

def deduce_winner(memory, values):
    game[memory[0], memory[1]] = values
    
    if -3 in np.sum(game, axis=1):
        print("Player 1 wins")
        return True
    elif 3 in np.sum(game, axis=1):
        print("Player 2 Wins")
        return True
    
    if -3 in np.sum(game, axis=0):
        print("Player 1 wins")
        return True
    elif 3 in np.sum(game, axis=0):
        print("Player 2 Wins")
        return True
        
    # two diagnals
    if game[0,0] + game[1,1] + game[2,2] == 3:
        print("Player 2 Wins")
        return True
    elif game[0,0] + game[1,1] + game[2,2] == -3:
        print("Player 1 Wins")
        return True
    
    if game[0,2] + game[1,1] + game[2,0] == 3:
        print("Player 2 Wins")
        return True
    elif game[0,2] + game[1,1] + game[2,0] == -3:
        print("Player 1 Wins")
        return True
    
    return False
        
if __name__ == "__main__":
  print("""
  Start the game by entering your player token, and then user input by (1,2) for placing the 'o' s and 'x' s on the game board
  """)
  player_1 = input("Enter 1st player token:")
  if player_1 == 'o':
    player_2 = 'x'
  elif player_1 == 'x':
    player_2 = 'o'
  else:
    raise Exception("Invalid token")
  
  previous = None
  while(True):
      user_input1 = input("Enter the user input for player 1: Enter '0,2' for placing it in 1st row and 3rd column")
      user_input=list(list(map(lambda x: int(x), user_input1.split(","))))
      previous = draw_game_board(
          user_input=user_input, 
          player=player_1,
          previous=previous
      )
      print(previous)
      if deduce_winner(user_input, -1):
        break
      user_input2 = input("Enter the user input for player 2")
      user_input=list(list(map(lambda x: int(x), user_input2.split(","))))
      previous = draw_game_board(
          user_input=user_input,
          player=player_2,
          previous=previous
      )
      print(previous)
      if deduce_winner(user_input, 1):
            break

```
