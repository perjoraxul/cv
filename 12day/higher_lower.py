import random


print("Welcome to the number guessing game! ")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

ATTEASY = 10
ATTHARD = 5
playAgain = True

while playAgain :
  numberIs = random.randint(0,100)
  atteasy = ATTEASY
  atthard = ATTHARD
  
  while atteasy and atthard != 0 :  
    if difficulty == "easy" :
      print(f"You have {atteasy} attempts remaining to guess the number. ")
      guess = input("Make a guess: ")
      if int(guess) == numberIs : 
        print(f"You are right! The number was indeed {numberIs}")
        break
      else : 
        if int(guess) > numberIs :
          print("Too high.")
        else : 
          print("Too low.")
        atteasy = atteasy - 1
        if atteasy != 0 : 
          print("Guess again.")
    else :
      print(f"You have {atthard} attempts remaining to guess the number. ")
      guess = input("Make a guess: ")
      if int(guess) == numberIs : 
        print(f"You are right! The number was indeed {numberIs}")
        break
      else : 
        if int(guess) > numberIs :
          print("Too high.")
        else : 
          print("Too low.")  
        atthard = atthard - 1
        if atthard != 0 : 
          print("Guess again.")
        
  if atteasy == 0 or atthard == 0 :
    print(f"You lost. The numbers was {numberIs}")
  break