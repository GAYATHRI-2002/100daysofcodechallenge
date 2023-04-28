myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("your tip 'choose 15,20, 25 percentage': "))

totalbillwithtip = tip / 100 * myBill + myBill
billperperson= totalbillwithtip / numberOfPeople

final_amount = round(billperperson, 2)


print("You all owe", final_amount)

