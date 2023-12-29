from getpass import getpass as input

import pyfiglet
font = pyfiglet.figlet_format("EPIC GAME")
print(font)

print ("Welcome to Epic Game")

print("Select your move(R,P, S)")
print()


# Input validation for Player1 
while True:
  player1move = input("Player1 move> ")
  if player1move in ["R", "P", "S"]:
    break
  else:
    print("Invalid move. Please enter R, P, or S")
print()

# Input validation for Player2
while True:
  player2move = input("Player2 move>")
  if player2move in ["R", "P", "S"]:
    break
  else:
    print("Invalid move. Please enter R,P, or S")
print()

# Game Logic

if player1move == player2move:
  print("Wow, its a tie!")

elif (player1move == "R" and player2move == "S") or (player1move == "P" and player2move == "R") or (player1move == "S" and player2move == "P"):
  print(f"Player1 wins! {player1move} beats {player2move}")
else:
  print(f"Player 2 wins! {player2move} beats {player1move}")


  