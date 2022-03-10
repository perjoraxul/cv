from art import *
from game_data import *
import random
import os 


def generate_item() : 
  rand_num = random.randint(0,len(data) - 1)
  followers = data[rand_num]['follower_count']
  return followers, data[rand_num]

def achoice() :
  choice = input("Who has more followers? Type 'A' or  'B' :")
  return choice

clear = lambda: os.system('cls')

print(logo)
generate_item()
answer = ''
score = 0

my_try = True
while my_try :
  if score > 0 :
    print(f"You're right! Current score: {score}")
    
  if score == 0 :
    a = generate_item()
    
  b = generate_item()

  print(f"Compare A: {a[1]['name']}, a/an {a[1]['description']}, from {a[1]['country']}.")
  print(vs)
  print(f"Against B: {b[1]['name']}, a/an {b[1]['description']}, from {b[1]['country']}.")
  c = achoice()
  
  
  if a[0] <= b[0] :
    answer = "B"
  else : 
    answer = "A"

  
  if answer == c :
    clear()
    score += 1
    a = b
    b = generate_item()
    while b[1] == a[1] :
      b = generate_item()
    
  else :
    clear()
    print(f"Sorry, that's wrong. Final score : {score}")
    my_try = False