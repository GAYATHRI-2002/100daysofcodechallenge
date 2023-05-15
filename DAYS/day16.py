from getpass import getpass as input

print("THE BATTLE BEGINS")
print("ROCK , PAPER, SCISSOR")
print()

player_1Score = 0
player_2Score = 0

while True:
  player_1 = input("player1> ")
  player_2 = input("player2> ")


  if player_1 == "R" and player_2 == "R" :
    print("both are same .... invali")
  elif player_1 == "R" and player_2 == "S":
    print(" player_1 smashed player_2")
    player_1Score += 1
  elif player_1 == "P" and player_2 == "P":
    print("invalid.....")
  elif player_1 == "S" and player_2 == "S":
    print("invalid choose the same item")
  elif player_1 == "S" and player_2 == "R":
    print(" player_1 loose aganist player_2")
    player_2Score += 1
  elif player_1 == "R" and player_2 == "P":
    print(" player_1 crushed player_2")
    player_1Score =+ 1
  elif player_1 == "S" and player_2 == "P":
    print(" player_1 destroyed player_2")
    player_1Score += 1
  elif player_1 == "P" and player_2 == "S":
    print(" player_2 destroyed player_1")
    player_2Score += 1
  elif player_1 == "P" and player_2 == "R":
    print(" player_2 destroyed player_1")
    player_2Score += 1

  print("player_1 has ", player_1Score, "wins.")
  print("player_2 has ", player_2Score, "wins.")
  if player_1Score ==3 or player_2Score == 3:
    print("Thanks for playing!")
    exit()
  else :
    continue
