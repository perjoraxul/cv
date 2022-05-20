import random
import hangman_art
import hangman_words

#list of words from which the computer will randomly select one imported from hangman_words
chosen_word = random.choice(hangman_words.word_list)

#this is only for testing purposes
print(f'The solution is {chosen_word}.')


display = []
lives = 6
in_game = True

#creating a list with number of "_" equal to the number of letters in chosen_word
for i in range(len(chosen_word)) : 
  display.append('_') #display += i

#printing the logo imported from "hangman_art"
print(hangman_art.logo)

#conditions for running
while "_" in display and in_game :
  
  #user input of a letter that user thinks it's in the word  
  guess = input("Guess a letter: ").lower()

  for i in display :
    if i == guess :
      print("You've already chose that letter!")
  
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
    #list with ASCII for displaying status imported from "hangman_art"
    print(hangman_art.stages[lives])
    if lives == 0 :
      in_game = False
      print("You lost!")
  print(f"{' '.join(display)}")
