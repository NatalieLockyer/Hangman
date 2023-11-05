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
print(f"Welcome to Hangman {username}, lets get started")


#Gets random word from games list