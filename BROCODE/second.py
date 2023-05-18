website = "http://google.com"
website2 = "http://instagram.com"
slice = slice(7,-4)
print(website[slice])
print(website2[slice])
-----------------------------------------------------------
age = int(input("how old are you?: "))

if age >= 18:
    print("you are an adult!")
elif age == 100:
    print("you are a century man")
elif age < 0:
    print("you haven't born yet")
else:
    print("you are a child")
    -------------------------------------------------------
    
    # logical operators 

temp = int(input("what is the temperature outside: "))

if not(temp >=0 and temp <= 30) :
    print (" the temperature good today")
    print("go out side")

elif not(temp < 0 or temp >30) :
    print("the temperature is bad today")
    
 --------------------------------------------------------------
name = None

while not name:
    name = input("enter the name: ")
print("hello "+name)
----------------------------------------------------------
#for loop

#for i in range(10):
    #print(i+1)

for i in range (50, 100+1, 2):
    print(i)
  ---------------------------
for seconds in range(20,0,-2):
    print(seconds)
    time.sleep(1)
print("HAPPY NEW YEAR")
-----------------------------------------------
#NESTED LOOP

row = int(input("how many rows: "))
column = int(input("how many columns: "))
symbol = input("what symbol should be printed: ")

for i in range (row):
    for j in range(column):
        print(symbol, end="")
    print()


