#Number Guessing Game

#Sumith Sai Koraboina

import random

numbers=[
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100
    ]
art="""
▀▄▀▄▀▄ ℕỮ𝓂β𝒆ｒ Ｇ𝓾Ⓔ𝐒丂 Ꮆ𝐚𝔪Ẹ ▄▀▄▀▄▀
"""
print(art)
lives="❤️"
print("Welcome to the number guess game")
difficulty_level=input("Select the game difficulty level ---> Easy 😉 or Hard 🥵 : ").lower()
#print(f"You chose {difficulty_level} level, and you have {no_of_lives} lives , All the best")
win=False
answer=random.choice(numbers)
easy="😏 "
hard=" 💀 "
if difficulty_level=="easy":
    no_of_lives=10
    emoji=easy
elif difficulty_level=="hard":
    no_of_lives=5
    emoji=hard
result="Lost"
print(f"You chose {difficulty_level} {emoji} level, and you have {no_of_lives}{lives} lives , All the best")
while no_of_lives!=0:
    guess=int(input("Choose the correct guess in between 1 and 100 : "))
    if guess==answer:
        print("You guessed it right, You Won 🏆 !")
        result=Win
        no_of_lives=0
        #win=True
    elif guess<answer:
        print("Too low")
        no_of_lives-=1
        if no_of_lives>0:
            print(f"You have {no_of_lives}{lives} lives remaining, Guess the number wisely 🤔 🧠 💭")
    elif guess>answer:
        print("Too high")
        no_of_lives-=1
        if no_of_lives>0:
            print(f"You have {no_of_lives}{lives} lives remaining, Guess the number wisely 🤔 🧠 💭")
        
if result=="Win":
    print(f"The correct answer is {answer} 🤯")
elif  result=="Lost":
    print(f"You Lost the game, The correct answer is {answer} 🤯")
