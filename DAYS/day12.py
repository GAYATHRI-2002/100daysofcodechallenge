print("EXAM GRADE GENERATOR")
print()
name = input("enter the name of the test : ")
mgrade = int(input("enter the maximum mark of the test : "))
grade = float(input("enter your mark: "))

nscore = float(grade/ mgrade)
final = round(nscore, 2)
final_perc = round(float(grade/mgrade)*100,2)

print("you got", final_perc,"%")


if final >= .90:
  print(" excellent , you are awarded A+ 🙌")
elif final <= .89 and final >= .80:
  print("your grade is A")
elif final <= .79 and final >= .70:
  print("your grade is B")
elif final <= .69 and final >= .60:
  print("your grade is C")
elif final <= .59 and final >= .50:
  print("your grade is D")
elif final <= .50:
  print("you are under 50")
else:
  print("try again")
  
