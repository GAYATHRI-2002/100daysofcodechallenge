length = int(input("enter the length: "))
breadth = int(input("enter the breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print("the area is: ",area)
print("the perimeter is: ", perimeter)


sub_1 = int(input("enter the first subject mark: "))
sub_2 = int(input("enter the second subject mark: "))
sub_3 = int(input("enter the third subject mark: "))
sub_4 = int(input("enter the fourth subject mark: "))

total = sub_1 + sub_2 + sub_3 + sub_4
average = total / 4

if total > 50:
    print("pass")
else:
    print("fail") 
