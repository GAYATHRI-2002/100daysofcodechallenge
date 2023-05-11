from getpass import getpass as input

print("THE BATTLE BEGINS")
print()
print(" your items are  R P S")
player_1 = input("enter your item: ")
player_2 = input("enter your item: ")

if player_1 == "R" and player_2 == "R" :
  print("both are same .... invali")
elif player_1 == "R" and player_2 == "S":
  print(" player_1 smashed player_2")
elif player_1 == "P" and player_2 == "P":
  print("invalid.....")
elif player_1 == "S" and player_2 == "S":
  print("invalid choose the same item")
elif player_1 == "S" and player_2 == "R":
  print(" player_1 loose aganist player_2")
elif player_1 == "R" and player_2 == "P":
  print(" player_1 crushed player_2")
elif player_1 == "S" and player_2 == "P":
  print(" player_1 destroyed player_2")
elif player_1 == "P" and player_2 == "S":
  print(" player_2 destroyed player_1")
elif player_1 == "P" and player_2 == "R":
  print(" player_2 destroyed player_1")
  
else :
  print("baaaaddddd")
