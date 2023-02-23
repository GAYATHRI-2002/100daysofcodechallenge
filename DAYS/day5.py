numbers = [3, 4, 5, 2, 1]
numbers.append(9)
print(numbers)

numbers = [3, 4, 5, 2, 1]
numbers.insert(0, 10)
print(numbers)

numbers = [3, 4, 5, 2, 1]
numbers.remove(5)
print(numbers)


numbers = [3, 4, 5, 2, 1]
numbers.clear()
print(numbers)

numbers = [3, 4, 5, 2, 1]
numbers.pop()
print(numbers)

numbers  = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for  number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques) 
