print("Welcome to the tip calculator!")
bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

totalBill = float(bill) * (int(tip) / 100 + 1) 

#rounds to 2 decimal places 
perPerson = round(totalBill / int(people), 2)

print(f"Each person should pay: {perPerson}")