import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

lista = ""

#pick random letters from "letters" list and form "lista" string
for l in range(1, nr_letters + 1):
  randNumber = random.randint(1, len(letters)-1)
  lista += letters[randNumber]

#pick random symbols from "symbols" list and add to "lista" string
for l in range(1, nr_symbols + 1):
  randNumber = random.randint(1, len(symbols)-1)
  lista += symbols[randNumber]  

#pick random numbers from "numbers" list and add to "lista" string
for l in range(1, nr_numbers + 1):
  randNumber = random.randint(1, len(numbers)-1)
  lista += numbers[randNumber] 

print(lista)

#set how many time the cycle of replacement will happen
randomNumber = random.randint(5, 10)

#convert "lista" string to "list1" list
list1 = list(lista)

#cycle of replacement - switch elements from random positions between them
for i in range(0,randomNumber) :
  num1 = random.randint(0, len(lista)-1)
  num2 = random.randint(0, len(lista)-1) 

  placeholder = list1[num1]
  list1[num1] = list1[num2]
  list1[num2] = placeholder

#convert "list1" list to "finalString" string
finalString = ""
for i in list1 : 
  finalString += i

print(finalString)



