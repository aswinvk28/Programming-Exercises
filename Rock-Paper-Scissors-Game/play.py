import random

class Win():
  def __init__(self, score):
    self.score = score
  
  def __str__(self):
    if self.score == 1:
      return "Congratulations, You Win!: " + str(self.score) + " Want to start a new game?"

class Lose():
  def __init__(self, score):
    self.score = score
  
  def __str__(self):
    if self.score == -1:
      return "You Lose! Want to start a new game!: " + str(self.score)

class Rock(object):
  type = 'rock'
  def __radd__(self, other):
    if other.type == 'scissors':
      return Lose(-1)
    elif other.type == 'paper':
      return Win(1)
  def __add__(self, other):
    if other.type == 'rock':
      return "Draw! Try again!"
    
class Scissors(object):
  type = 'scissors'
  def __radd__(self, other):
    if other.type == 'rock':
      return Win(1)
    elif other.type == 'paper':
      return Lose(-1)
  def __add__(self, other):
    if other.type == 'scissors':
      return "Draw! Try again!"

class Paper(object):
  type = 'paper'
  def __radd__(self, other):
    if other.type == 'rock':
      return Lose(-1)
    elif other.type == 'scissors':
      return Win(1)
  def __add__(self, other):
    if other.type == 'paper':
      return "Draw! Try again!"

if __name__ == "__main__":
  
  while(True):
    print("""
          Enter r for Rock, 
                s for Scissors, 
                p for Paper
          """)
    player_1 = input("Player 1: ")
    player_type = input("Press c for computer to play or h for human to play:")
    
    if player_1 == 'r':
      player_1 = Rock()
    elif player_1 == 's':
      player_1 = Scissors()
    elif player_1 == 'p':
      player_1 = Paper()
      
    if player_type == 'h':
      player_2 = input("Player 2: ")
      if player_type == 'h':
        if player_2 == 'r':
          player_2 = Rock()
        elif player_2 == 's':
          player_2 = Scissors()
        elif player_2 == 'p':
          player_2 = Paper()
    elif player_type == 'c':
      player_2 = random.choice([Rock(), Scissors(), Paper()])
      
    print(player_1 + player_2)
    
