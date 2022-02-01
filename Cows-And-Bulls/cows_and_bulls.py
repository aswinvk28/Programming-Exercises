import random
import math

def generate_n_digit_random_number(n_digits=4):
  number = 0
  for i in range(n_digits):
    number += random.randint(0,9) * 10**(n_digits-i-1)
  
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
  return (cows, bulls)

if __name__ == "__main__":
  
  number = generate_n_digit_random_number(4)
  result = guess_number(number)
  print("Cows: ", result[0], " Bulls: ", result[1], " Number: ", number)
  
