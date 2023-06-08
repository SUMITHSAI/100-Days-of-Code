#Challenge 1 Solution

#SUMITH SAI KORABOINA

#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word= random.choice(word_list)
# print(chosen_word)TODO1
#

guess=input("Guess a letter from the wordlist\n")
#TODO 2

for x in chosen_word:
  if x==guess:
    print("Correct Guess")
  else:
    print("Wrong Guess")
    #TO DO 3