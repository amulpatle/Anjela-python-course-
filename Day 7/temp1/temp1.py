import random


word_list = ["amul", "Aditya", "Ashish","seju","mansi","nikki"]

chosen_word = random.choice(word_list)

print(chosen_word)

word = input("Guess a word from list").lower()

l = len(word_list)

# for i in range(l):
#     s = len(word_list)
#     for j in range(s):
#         if(word == word_list[i][s]):
#             print("right")
#         else:
#             print("Wrong")

for i in chosen_word:
    if word == i:
        print("right")
    else:
        print("wronge")