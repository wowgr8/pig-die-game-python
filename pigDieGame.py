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

max_score = 50
# list comprehension - puts 0 inside of list for every player we have
player_scores = [0 for _ in range(players)]

# This loop continues until a player reaches the maximum score
while max(player_scores) < max_score:

  # Loop through each player
  for player_idx in range(players):
    # Display player information
    print("\nPlayer number", player_idx + 1, "your turn has just started!\n")
    print("Your total score is:", player_scores[player_idx], "\n")
    current_score = 0

    # Inner loop for the player's turn
    while True:
      # Ask the player if they want to roll
      should_roll = input("Would you like to roll (y)? ")
      # Exit the inner loop if the player chooses not to roll
      if should_roll.lower() != "y":
        break

      # Roll the dice and get the value
      value = roll()
      # If the value is 1, end the player's turn
      if value == 1:
        print("You rolled a 1! Your turn is over!")
        current_score = 0
        break
      else:
        # Update the current score and display the rolled value
        current_score += value
        print("You rolled a:", value)

      # Display the current score during the turn
      print("Your score is:", current_score)

    # Update the player's total score
    player_scores[player_idx] += current_score
    print("Your total score is:", player_scores[player_idx])

# Determine the winner and display the result
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)





