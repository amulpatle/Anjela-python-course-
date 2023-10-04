import random

li = ["amul", "aditya", "mansi", "ankit", "nikki", "pratik","saurav", "ashish"]

choosen_word = random.choice(li)
print(choosen_word)

display = []

for i in range(len(choosen_word)):
    display+="_"

print(display)

# letter = input("Guess a Letter ").lower()

for j in range(len(choosen_word)):
    letter = input("Guess a Letter ").lower()
    for i in range(len(choosen_word)):
        if letter == choosen_word[i]:
            display[i] = letter
    if letter == choosen_word[i]:
        print(display)
    else:
        print("lost a life")

