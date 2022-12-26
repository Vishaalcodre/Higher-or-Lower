# Add art
from art import logo,vs
from game_data import data
from replit import clear
import random

def account(data):
  account_name = data['name']
  account_description = data['description']
  account_country = data['country']
  return f"{account_name}, {account_description}, from {account_country}."

def check_ans(guess,data_a,data_b):
  if data_a>data_b:
    return guess == 'a'
  else:
    return guess == 'b'

# Generate a random account from the game data.
data_b = random.choice(data)

#Score Keeping.
score = 0
print(logo)
continue_game = True

# Make game repeatable.
while continue_game:
  # Make B become the next A.
  data_a = data_b
  data_b = random.choice(data)
  
  # Get follower count.
  account_follower_a = data_a['follower_count']
  account_follower_b = data_b['follower_count']
  
  
  while data_a == data_b:
    data_b = random.choice(data)
  
  
  
  
  
  print(f"Compare A: {account(data_a)}")
  print(vs)
  print(f"Against B: {account(data_b)}")
  print()

  # Ask user for a guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  # Check if user is correct.
  is_correct = check_ans(guess,account_follower_a,account_follower_b)

  # Clear screen between rounds.
  clear()
  print(logo)
  
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    continue_game = False
    print(f"Sorry that's wrong. Final score: {score}")
