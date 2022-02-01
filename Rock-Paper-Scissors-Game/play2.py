import random 

def win():
  return "Congratulations, You Win! Want to start a new game?"

def lose():
  return "You Lose! Want to start a new game?"

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
  
  