import random

def roll():
  min_value = 1
  max_value = 6
  roll = random.randint(min_value, max_value)

  return roll

# This checks if user input is a valid number of players
while True:
  players = input("Enter the number of players (2 - 4): ")
  # isdigit will tell us if it's a valid whole number or not
  if players.isdigit():  
    # Converts user input string into a integer
    players = int(players)
    if 2 <= players <= 4:
      break
    else:
      print("Must be between 1 -4 players.")
  else:
    print("Invalid, try again.")

