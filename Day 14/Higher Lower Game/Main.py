from art import logo
from art import vs
from gamedata import data
import random

print(logo)

def check_answer(guess,a_follower,b_follower):
    if(a_follower>b_follower):
        return guess == a_follower
    else:
        return guess == b_follower



# generate a rangom account from data set
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)
# print(account_a)

# formate the account data into pritable formate

def formate_data(account):
    """Formate the account data into the printable formate"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    account_follower_count = account["follower_count"]
    return f"{account_name}, a {account_desc},from {account_country}"
def check_answer(guess, follower_a, follower_b):
    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"



print(f"compare a : {formate_data(account_a)}")
print(vs)
print(f"Against b : {formate_data(account_b)}")

# Ask user for a guess

a_follower_account = account_a["follower_count"]
b_follower_account = account_b["follower_count"]
guess = input("who has more follower? type A or B :").lower()

is_correct = check_answer(guess,a_follower_account,b_follower_account)

if(is_correct):
    print("You're right")
else:
    print("you're wronge")