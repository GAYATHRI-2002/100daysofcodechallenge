numbers = [5, 2, 5, 2, 2]
for i in  numbers:
    print('g' * i) 
    //////////////////////////////////////
    
    names = ['john', 'ravi', 'maya','arya','devu']
names[0] = 'meena'
print(names)
   
#find the largest number

numbers = [3, 5, 7, 2, 1, 9]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max) 

# car game

command = ""
started = False
while True:
    command = input("> ").lower()
    if command  == "start":
        if started:
            print("car is already  started")
        else:
            started = True    
        print("car started......")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started =  False    
        print("car stopped..........")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """) 
    elif command == "quit":
        break    
    else:
        print("i don't understand")       

