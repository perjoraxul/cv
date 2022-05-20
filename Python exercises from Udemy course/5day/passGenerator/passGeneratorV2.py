import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

lista = []

#pick random letters from "letters" list and form "lista" string
for l in range(1, nr_letters + 1):
    lista.append(random.choice(letters))

#pick random symbols from "symbols" list and add to "lista" string
for l in range(1, nr_symbols + 1):
    lista.append(random.choice(symbols))  

#pick random numbers from "numbers" list and add to "lista" string
for l in range(1, nr_numbers + 1):
    lista.append(random.choice(numbers))

print(lista)

random.shuffle(lista)

#convert "lista" list to "finalString" string
finalString = ""
for i in lista : 
  finalString += i

print(finalString)



