print("Fill in the blank lyrics!")
print()
print()
print("{ type in the blank lyrics and see if you are as cool as me .}")
print()
print()

counter = 1
while  True:
  print("never going to _______ you up.")
  blank = input("enter the word missing in the line : ")
  if blank == "give":
    
    print("Well done! It only took you ", counter,"attempts")
    break
  else:
    print("Nope, try again .")
    counter += 1
