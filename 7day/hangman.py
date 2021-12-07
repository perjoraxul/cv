import random

#stages" list with ASCII for displaying status
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#list of words from which the computer will randomly select one
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#this is only for testing purposes
print(f'The solution is {chosen_word}.')


display = []
lives = 6
in_game = True

#creating a list with number of "_" equal to the number of letters in chosen_word
for i in range(len(chosen_word)) : 
  display.append('_') #display += i

#conditions for running
while "_" in display and in_game :
  
  #user input of a letter that user thinks it's in the word  
  guess = input("Guess a letter: ").lower()

  countt = 0
  right_count = len(chosen_word)

  #iterate through chosen_word  
  for i in chosen_word : 
    #if the user's letter is in the computer selected word, replace the "_" in "display" with the letter (in the same location) 
    if i == guess : 
      display[countt] = guess
      right_count += 1
    countt += 1
  #the condition for winning the game is to not have any "_" in "display" (as all the "_" will be replaced with guessed letters)  
  if not "_" in display :
    print("You win!")
    
  #if "right_count" is equal to the length of "chosen_word" it means no letter was found in this iteration, that exists in "chosen_word" (because "right_count" remains unchanged ( right_count = len(chosen_word))) 
  if right_count == len(chosen_word) :  
    lives -= 1
    print(f"You have {lives} more lives.")
    print(stages[lives])
    if lives == 0 :
      in_game = False
      print("You lost!")
  print(f"{' '.join(display)}")
