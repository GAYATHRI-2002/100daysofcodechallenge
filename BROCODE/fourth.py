# 2D list
drinks = ["soda", "tea", "coffee"]
dinner = ["cake"," burger", "hotdog", "pizza"]
dessert = ["icecream", "juice"]

food = [drinks, dinner , dessert]

print(food[0][2])   # in here it only print drink list with coffee element only
--------------------------------------------------------------------------------------------

#tuples : the are collections which can be ordered and changeble

student = ("Ben", 23, "male")

print(student.count("Ben"))
print(student.index(23))

for x in student:
    print(x)

if "Ben" in student:
    print("Ben is here")
    
---------------------------------------------------------------------------------------------------------------------------------------------------


