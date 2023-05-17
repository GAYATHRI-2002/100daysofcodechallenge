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
