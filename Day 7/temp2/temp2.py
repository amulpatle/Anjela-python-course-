import random

li = ["amul", "aditya", "mansi", "ankit", "nikki", "pratik","saurav", "ashish"]

choosen_word = random.choice(li)
print(choosen_word)

display = []

for i in range(len(choosen_word)):
    display+="_"

print(display)

