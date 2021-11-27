#Simple script that picks a random person who will pay the meal.
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

leng = len(names)
ran = names[random.randint(0, leng-1)]

print(ran + " is going to buy the meal today!")