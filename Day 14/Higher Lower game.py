#Higher Lower game

#Sumith sai Koraboina

from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()

'''

FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

'''



# Generate a random account from the game data.

# Format account data into printable format.

# Ask user for a guess.

# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.

# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.

#Code I tried and written with errors

import random
from art import logo
from art import vs
from game_data import data
print(logo)

list1=[]
def choose():
  found1=random.choice(data)
  for i in found1:
    need1=found1[i]
    list1.append(need1)

list2=[]
def pick():
  found2=random.choice(data)
  for i in found2:
    need2=found2[i]
    list2.append(need2)

choose()
pick()
A=list1[1]
B=list2[1]
final=False
# print(A)
# print(B)
#large="D"
# def check():
#   if A>B:
#     large="A"
#     #return large
#   elif A<B:
#     large="B"
#     #return large
#   else:
#     large="A"
    #return large
      
while not final:
  print(f"Comapre A : {list1[0]}, {list1[2]}, {list1[3]}.")
  print(vs)
  print(f"Against B : {list2[0]}, {list2[2]}, {list2[3]}.")
  # def check():
  #   if A>B:
  #     max="A"
  #   elif A<B:
  #     max="B"
  #   else:
  #     max="A"
  
  choice=input(f"Who has more Followers? Choose A or B: ")
  print(choice)
  # def check():
  #   if A>B:
  #     large="A"
  #   #return large
  #   elif A<B:
  #     large="B"
  #   #return large
  #   else:
  #     large="A"

  # check()
  if choice=="A" and int(A)>int(B):
    C=A
    A=0
    pick()
    B=list2[1]
    print(f"{choice} is Correct")

  elif choice=="B" and int(B)>(A):
    C=B
    B=0
    choose()
    A=list1[1]
    print(f"{choice} is correct")

  else:
    final=True
    print("Lost")