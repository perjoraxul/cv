print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

count1 = 0
count2 = 0

#concatenate strings and convert all the letters to lower case
name_combined_lower = (name1 + name2).lower()

#check how many times the letter passed as an argument in "count()" function, finds itself in both names
n1 = name_combined_lower.count("t")
n2 = name_combined_lower.count("r")
n3 = name_combined_lower.count("u")
n4 = name_combined_lower.count("e")
nt = n1 + n2 + n3 + n4 

N1 = name_combined_lower.count("l")
N2 = name_combined_lower.count("o")
N3 = name_combined_lower.count("v")

Nt = N1 + N2 + N3 + n4

nString = str(nt) + str(Nt)

if nt == 0 or nt >= 9:
  print(f"Your score is " + nString + ", you go together like coke and mentos.")
elif nt == 4 or (nt == 5 and Nt == 0) :
  print("Your score is " + nString + ", you are alright together.")
else : 
  print("Your score is " + nString + ". It's a match.")