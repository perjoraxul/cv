print("Welcome to the tip calculator!")
bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

totalBill = float(bill) * (int(tip) / 100 + 1) 

perPerson = round(totalBill / int(people), 2)

finalAmount = "{:.2f}".format(perPerson)

print(str(type(perPerson)) + " " + str(type(finalAmount)))
print(f"Each person should pay: ${finalAmount}")