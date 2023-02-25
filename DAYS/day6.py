#tuples
numbers = (1, 2, 3)
print(numbers[0])

#unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates
print(y)

customer = {
    "name": "john smith",
    "age": 30,
    "is_verified": True
}
customer ["name"] = "will smith"  #updated the name
print(customer["name"])

phone = input("phone : ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)    

#functions
def greet_user():
    print('hi there!')
    print('welcome home')


print("start")
greet_user() 
print("finish") 


def greet_user(name):
    print(f'hi {name}')
    print('welcome home')


print("start")
greet_user("john")
greet_user("smith") 
print("finish")   
