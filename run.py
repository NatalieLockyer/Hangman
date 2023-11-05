#To randomise words and to add stages of the hangman one a life is lost
import random, hangman_tries

#Access to the list of words 
from words import secret_word_list

#Game title 
print("<>    <>     <><>     <>      <>    <>>>>>>    <>        <>     <><>     <>      <>")
print("<>    <>    <>  <>    <>>>    <>   <>     <>   <>>>    <<<>    <>  <>    <>>>    <>")
print("<><<>><>   <><<>><>   <>  <>  <>   <>          <>  <<>>  <>   <><<>><>   <>  <>  <>")
print("<>    <>   <>    <>   <>    <<<>   <>  >>>>>   <>   <>   <>   <>    <>   <>    <<<>")
print("<>    <>   <>    <>   <>      <>    <<<<<<     <>        <>   <>    <>   <>      <>")

print("------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------")

#Enter your name
username = input("Please enter your name: ")
print("\n")
print(f"Welcome to Hangman {username}!\n")

def get_word(secret_word_list):
    """
    This function returns a random word from secret_word_list
    """
    return random.choice(secret_word_list)

def display_secret_word(secret_word):
    """
    This function is to display the secret word, and replace the letters with underscores"""
    print(" _ " * len(secret_word))

def guess_the_letter(guessed_letter, secret_word):
    """
    This function asked the user to guess a letter,
    if user has already used that letter - print - already been used
    wrong letter - print - incorrect letter
    correct letter - print - correct letter 
    """
    guessed_letter = ""
    attempts_left = 6

    while not guessed_letter and attempts_left == 0:
        guess = input("Please enter a letter: ").lower()
        if len(guess) > 1 and guessed_letter.isalphha():
            print("Only single letters are allowed, please try again")
        elif guess in guessed_letter:
            print("You have already tried the letter", guess)
        elif guess not in secret_word:
            print(guess, "is not in the word")
            attempts_left -= 1
            guessed_letter.append(guess)
        else:
            print(f"Well done {username}, you guessed the correct letter")
            guessed_letter.append(guess)
        


print(f"To begin, please choose your first letter. \n")

secret_word = get_word(secret_word_list)
display_secret_word(secret_word) 
guess_the_letter(guess_the_letter, secret_word)

print(hangman_tries.get_hangman_stage(attempts_left))

