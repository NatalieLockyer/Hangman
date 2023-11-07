# To randomise words and to add stages of the hangman one a life is lost
import random

# Acces to hangman_tries.py
import hangman_tries

# Access to the list of words 
from words import secret_word_list

# Game title 
print("<>    <>     <><>     <>      <>    <>>>>>>    <>        <>     <><>     <>      <>")
print("<>    <>    <>  <>    <>>>    <>   <>     <>   <>>>    <<<>    <>  <>    <>>>    <>")
print("<><<>><>   <><<>><>   <>  <>  <>   <>          <>  <<>>  <>   <><<>><>   <>  <>  <>")
print("<>    <>   <>    <>   <>    <<<>   <>  >>>>>   <>   <>   <>   <>    <>   <>    <<<>")
print("<>    <>   <>    <>   <>      <>    <<<<<<     <>        <>   <>    <>   <>      <>")

print("------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------")

#create a menu page with option
#eg 1. Start a new game
#   2. Game instructions 
#   3. exit the game

def welcome():
    """
    This function asks the user to input their name
    if user doesnt enter a character, an error
    message will appear.
    """
    print("Welcome to Hangman!")
    username = input("Please enter your name: ").strip()
    while username == "":
            username = input("You havent entered anything...Please enter your name:").strip()
    print(f"Welcome to Hangman {username}!\n")
    return username

def select_random_word(secret_word_list):
    """
    This function returns a random word from secret_word_list
    """
    return random.choice(secret_word_list)

def display_secret_word(secret_random_word, guessed_letters):
    """
    This function is to display the secret word, and replace the letters with underscores
    """
    display = ' '.join([letter if letter in guessed_letters else ' _ ' for letter in secret_random_word])
    print(display)

def guess_the_letter(guessed_letters, secret_random_word):
    """
    This function asks the user to guess a letter,
    if user has already used that letter - print - already been used
    wrong letter - print - incorrect letter
    correct letter - print - correct letter 
    """
    attempts_left = 6
    guessed = False
    while not guessed and attempts_left > 0:
        print(hangman_tries.get_hangman_stage(attempts_left))
        display_secret_word(secret_random_word, guessed_letters)
        guess = input("Please select a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed the letter", guess)
            elif guess not in secret_random_word:
                print("The letter", guess, "is not in the word.")
                attempts_left -= 1
                guessed_letter.append(guess)
            else:
                print("Well done", guess, "is in the word.")
                guessed_letter.append(guess)
                if all (letter in guessed_letters for letter in secret_random_word):
                    guessed = True
                    print("Congratulations! You have guess the word correctly.")

        else:
            print("Invalid entry. Please enter a single alphabetic charactor.")
    
    if not guess:
        print("Sorry, you have run out of attempts. The word was: ", secret_random_word)


def start_game():
    """
    """
    player_name = welcome()
    secret_random_word = select_randon_word(secret_word_list)
    guessed_letters = []
    print(f"The word has been chosen {player_name}. Lets play Hangman!")
    guess_the_letter(guessed_letters, secret_random_word)
