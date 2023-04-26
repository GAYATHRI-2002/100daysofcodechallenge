myPi = float(input("What is Pi to 3dp? "))
if myPi == 3.142 :
  print("Exactly!")
else:
  print("Try again 😭")
------------------------------------------------------------

score = int(input("What was your score on the test? "))
if score >= 80:
  print("Not too shabby")
elif score > 70:
  print("Acceptable.")
else:
  print("Dude, you need to study more!")
------------------------------------------------------------------------

start = int(input("enter your starting birth year: "))
end = int(input("enter your ending birth year:  "))
if start >= 1925 and end <= 1946 :
  print("oh your are traditionalists")
elif start >= 1947 and end <= 1964 :
  print("oh your are baby boomers")
elif start >= 1965 and end <= 1981 :
  print("oh your are generation x")
elif start >= 1982 and end <= 1995 :
  print("oh your are millenials")
elif start >= 1996 and end <= 2015 :
  print("oh you are generation z")
else:
  print(" you are an alien👽")
