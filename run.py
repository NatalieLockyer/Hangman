#Random words
import random

#Access to the list of words 
from words import secret_word_list

#Game title 
print("Hangman")
print("-----------------------------")

#Enter your name
username = input("Please enter your name: ")
print("\n")
print(f"Welcome to Hangman {username}, lets get started!")

# Select random word from secret word list
def select_word(secret_word_list):
    return random.choice(secret_word_list)

print(select_word(secret_word_list))