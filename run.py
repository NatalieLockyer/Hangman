import gspread
from google.oauth2.service_account import Credentials

# To randomise words
import random

# Access to hangman_tries.py
import hangman_tries

# Access to the list of words 
from words import secret_word_list

# To clear the screen
import os

# To Import Figlet
from pyfiglet import Figlet

# To import Data Frames
import pandas as pd

# To import frame to put around game
import tkinter as tk

font = Figlet(font='acrobatic', justify='center')


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('leaderboard.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_leaderboard')


def main_page():
    clear()
    print(font.renderText('HANG'))
    print(font.renderText('MAN'))
    print("Welcome to Hangman!")
    print("\nMain Menu")
    print("[1] To start a New Game")
    print("[2] Game Instructions")
    print("[3] Scoreboard")
    print("[4] Exit the game")
    option = input("\nPlease enter your selection (1, 2, 3 or 4): ")
    if option in main_page_option.keys():
        print(f"\nYou selected option {option}\n")
        return main_page_option[option]()
    else:       
        option > 4 or option < 1
        print("This is an invalid selection, Please enter 1, 2, 3 or 4: ")
        main_page()


def game_instructions():
    """
    This functions shows the game instructions
    when option 2 is selcted from the main menu
    """
    clear()
    print("Hangman Instructions")
    print("\nThe object of the game is the guess the secret")
    print("word, before the stick figure is hung.")
    print("\nYou will select letters from your keyboard to try and ")
    print("and solve the word")
    print("\nYou have a limited number of goes, so think carefully")
    print("\nGood Luck!!")
    input("\nPress ENTER to continue")
    clear()
    return main_page()


def scoreboard_data():
    """
    Function for calling the data
    """
    clear()
    SHEET = GSPREAD_CLIENT.open('hangman_leaderboard').sheet1
    data = SHEET.get_all_records()
    data_frame = pd.DataFrame(data)
    data_frame = data_frame.sort_values(by='guesses')
    print(font.renderText("SCORE"))
    print(font.renderText("BOARD"))
    print(data_frame.to_string(columns=['username', 'guesses'],))

    input("\nPress ENTER to return to continue to Main Page ")
    clear()
    return main_page()


def update_scoreboard_data(scoreboard_data):
    """
    Function
    """
    
    

def welcome():
    """
    This function asks the user to input their name
    if user doesnt enter a character, an error
    message will appear.
    """    
    username = input("Please enter your name: ").strip()
    while username == "":
        username = input("You havent entered anything...Please enter your name:").strip()
    clear()
    print(f"\nWelcome to Hangman {username}!\n")
    return username

    menu_option = main_page
    if menu_option == 4: 
        end_game = True
        print("Goodbye")
    elif menu_option == 3:
        leaderboard()
    elif menu_option == 2:
        game_instructions()
        display_secret_word(secret_random_word, guessed_letters)
    else:
        start_game()
    
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
    if there is a duplicate letter - print - already been chosen 
    wrong letter - print - incorrect letter
    correct letter - print - correct letter 
    """
    attempts_left = 6
    guessed = False
    end_game = False

    while not guessed and attempts_left > 0:
        print(hangman_tries.get_hangman_stage(attempts_left))
        display_secret_word(secret_random_word, guessed_letters)
        guess = input("\nPlease select a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("\nYou have already guessed the letter", guess)
            elif guess not in secret_random_word:
                print("\nThe letter" , guess, "is not in the word.")            
                attempts_left -= 1
                guessed_letters.append(guess)
            else:
                print("\nWell done", guess, "is in the word.")
                guessed_letters.append(guess)
                if all (letter in guessed_letters for letter in secret_random_word):
                    guessed = True
                    print("\nCongratulations! You have guessed the word correctly.")
            
            
        else:
            print("Invalid entry. Please enter a single alphabetic charactor.")
    

    if attempts_left == 0:
        print(hangman_tries.get_hangman_stage(attempts_left))
        end_game = True
        print("Unfortunately, you have run out of attempts. The word was: ",secret_random_word)


    play_again = input("\nDo you want to play again? Y or N ").lower()
    if play_again not in ["y", "n"]:
        print("Invalid input, please enter Y or N")
    elif play_again == "y":
        clear()
        start_game()
    else: 
        print("Thank you for playing Hangman, I hope you enjoyed it!")
        return main_page()            


def clear():
    """
    This function is to clear the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def start_game():
    """
    """
    username = welcome()
    secret_random_word = select_random_word(secret_word_list)
    guessed_letters = []
    print(f"The secret word has been chosen for you {username}. Lets play!")
    guess_the_letter(guessed_letters, secret_random_word)

main_page_option = dict({
    "1": start_game,
    "2": game_instructions,
    "3": scoreboard_data,
    "4": exit
})


main_page()


if __name__ == "__main__":
    start_game()

