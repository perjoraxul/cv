import art
import os

#define clear function which clears the console
clear = lambda: os.system('cls')


bids = {}
condition = True
bidsValue = []

print(art.logo)
print("Welcome to the secret auction program.")

#function that takes the name and bid input and adds to "bids" dictionary)
def auction() :
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid

#function that calculates the winner of the auction based on that biggest bid
def calculatingWinner() :
    #append the values from "bids" dictionary, to "bidsValue" list 
    for _ in bids :
        bidsValue.append(bids[_])
    
    #sort in ascending order the "bidsValue" list
    bidsValue.sort()
    # get the last value from "bidsValue" list, that is implicitly the highest value in that list
    maxValue = bidsValue[-1]
    #function that will be called with the parameter "maxValue" and will return the matched key from the "bids" dictionary for that value
    def get_key(val):
        for key, value in bids.items():
          if val == value:
              return key

    print(get_key(maxValue),"won with",maxValue,"dollars!")

#loop that verifies if there are any other bidders and if there aren't, it will exit
while condition :
    #calling "auction() function to save input name and bid"
    auction()   
    again = input("Are there any other biders? Type 'yes' or 'no' .")
    #clearing console for readability
    clear()
    #check if there are any other bidders and if not, change "condition" to False, for breaking out the "while" loop
    if again == "no" :
        condition = False

#calling "calculatingWinner()" function
calculatingWinner()
