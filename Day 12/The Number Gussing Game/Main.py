print("Welcome To The Number Gussing Game!")

import random

cChoice = random.randint(1,100)
# print(cChoice)

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
userInput = int(input("Make a guss"))
while attempts != 0:
    # userInput = input("Make a guss")
    if(userInput == cChoice):
        print("You Won!")
        break
    elif userInput<cChoice:
        print("Too low")
        attempts -= 1
        print(f"you Have {attempts} attemps left remaing to guess the number")
    
    else:
        print("Too high")
        attempts -=1
    userInput = int(input("Guess Again"))

if attempts == 0:
    print("You lose")