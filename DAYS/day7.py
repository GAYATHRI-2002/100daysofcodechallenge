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
    
    
factorial = 1
num = int(input("enter the number to find the factorial: "))
for i in range(1,num+1): 
    factorial = factorial*i
print(factorial)     


num = int(input("enter the total number : "))
for i in range(num,0,-1):
   print(i)    

number = int(input("enter the number: "))
for i in range(1,number + 1):
    if number % i ==0:
        print(i)
