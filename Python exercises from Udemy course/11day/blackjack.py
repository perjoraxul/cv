## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

'''
1.choose from cards[] and give 2 to player
2. chose from cards[] and assign 1 to computer
3.ask the player if he wants another card or stay
  4. if user wants another card, choose from cards[] and give 1 to player
      if sumOfPlayer cards > 21
          You are busted
      else
        repeat 4
  5.else 
    6.choose 1 card and give to computer
    if computer has sumOfCards < 17
      repeat 6
    else 
      if sumPlayaaer < sumComputer
          you lost
elif sumplayer > sumComputer
      you win
else 
      its a draw
'''
from art import *
import random as rd


print(logo)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def generateRand() : 
  return rd.randint(0,len(cards) - 1)

def appendCards(listName) : 
  listName.append(cards[generateRand()])
  
def playing() : 
  playerCards = []
  computerCards = []
  appendCards(playerCards)
  appendCards(playerCards)
  appendCards(computerCards)
  condition = True
  while condition :
    print("You have ", *playerCards) 
    print("Computer has ",*computerCards) 
    question = input("Do you want more cards? type 'yes' for yes and anything else for no")
    if question == 'yes' :
      appendCards(playerCards)
      if sum(playerCards) > 21 :
        print("You have ", *playerCards) 
        print("Computer has ",*computerCards)
        print(f"You are busted with {sum(playerCards)}!")
        break
    else : 
      condition = False
  while sum(playerCards) <= 21 :        
    while sum(computerCards) < 17 :
        appendCards(computerCards)
    if sum(computerCards) > 21 : 
        print("You have ", *playerCards) 
        print("Computer has ",*computerCards)
        print(f"Computer is busted with {sum(computerCards)}")         
    elif sum(computerCards) < sum(playerCards) : 
        print("You have ", *playerCards) 
        print("Computer has ",*computerCards)
        print(f"You won with {sum(playerCards)} against {sum(computerCards)}")
    elif sum(playerCards) < sum(computerCards):
        print("You have ", *playerCards) 
        print("Computer has ",*computerCards)
        print(f"You lost with {sum(playerCards)} against {sum(computerCards)}")
    else: 
        print("You have ", *playerCards) 
        print("Computer has ",*computerCards)
        print("It's a draw! ")
        
    again = input("Do you want to play again? yes = 'yes'; anything else = 'no ")
    if again == "yes" :
        playing()
    else : 
        break
    
playing()