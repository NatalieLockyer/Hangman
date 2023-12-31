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

font = Figlet(font='banner', justify='center')


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds1.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_leaderboard')
username = ""
guesses = 0


def main_page():
    """
    This function is the main page of the game.
    This holds the game Title, The 4 main menu options,
    and asks the user for thier menu selection
    """
    main_page_option = {
        "1": start_game,
        "2": game_instructions,
        "3": scoreboard_data,
        "4": exit_game
    }
    clear()
    print(font.renderText('HANGMAN'))
    print("Welcome to Hangman!\n")
    print("Main Menu - To begin select number")
    print("[1] To start a New Game")
    print("[2] Game Instructions")
    print("[3] Scoreboard")
    print("[4] Exit the game")
    option = input("\nPlease enter your selection (1, 2, 3, or 4):\n")
    if option in main_page_option:
        main_page_option[option]()
    else:
        print("This is an invalid selection, Please enter 1, 2, 3, or 4: ")
        main_page()


def exit_game():
    """
    This function will exit the user from the game.
    """
    print("Goodbye")
    exit()


def game_instructions():
    """
    This functions shows the game instructions
    when option 2 is selcted from the main menu
    """
    clear()
    print(font.renderText('RULES'))
    print("\nHangan is a word guessing game.")
    print("\nThe object of the game is to guess the secret")
    print("word, before the stick figure is hung.")
    print("\nYou will select letters from your keyboard to try and ")
    print("and solve the word.")
    print("\nYou have a limited number of goes, so think carefully")
    print("\nGood Luck!!")
    input("\nPress ENTER to continue\n")
    clear()
    return main_page()


def scoreboard_data():
    """
    This functions shows the scoreboard created in
    google sheets when option 2 is selcted from the
    main menu
    """
    clear()
    SHEET = GSPREAD_CLIENT.open('hangman_leaderboard').sheet1
    data = SHEET.get_all_records()
    data_frame = pd.DataFrame(data)
    data_frame = data_frame.sort_values(by='guesses')
    print(font.renderText("SCORE"))
    print(font.renderText("BOARD"))
    print(data_frame[['username', 'guesses']].to_string(index=False))

    input("\nPress ENTER to return to continue to Main Page\n")
    clear()
    return main_page()


def update_scoreboard(username, guesses, secret_random_word, guessed_letters):
    """
    This function is used to update the scoreboard in google sheets
    with the username and number of guesses
    """
    if all(letter in guessed_letters for letter in secret_random_word):
        worksheet = SHEET.worksheet("sheet1")
        new_row = [username, guesses]
        worksheet.append_row(new_row)


def welcome():
    """
    This function appears once the user has selected option 1
    to start a new game. It asks the user to input their name
    if user doesnt enter a character, an error
    message will appear.
    """
    global username
    if username == '':
        username = input("Please enter your name:\n").strip()
        while username == "":
            username = input("Invalid...Please enter your name:\n").strip()
        clear()
        print(f"\nWelcome to Hangman {username}!\n")
    else:
        print(f"\nWelcome back to Hangman, {username}!\n")


def select_random_word(secret_word_list):
    """
    This function returns a random word from secret_word_list
    """
    return random.choice(secret_word_list)


def display_secret_word(secret_random_word, guessed_letters):
    """
    This function is to display the secret word
    and replace the letters with underscores
    """
    display = ' '.join(
        letter if letter in guessed_letters else ' _ '
        for letter in secret_random_word
        )
    print(display)


def guess_the_letter(username, guessed_letters, secret_random_word):
    """
    This function asks the user to guess a letter,
    if there is a duplicate letter - print - already been chosen
    wrong letter - print - incorrect letter
    correct letter - print - correct letter
    Also includes a win message & lose message.
    Asks the player if they wish to play again
    """
    global guesses
    attempts_left = 6
    guessed = False

    while not guessed and attempts_left > 0:
        print(hangman_tries.get_hangman_stage(attempts_left))
        display_secret_word(secret_random_word, guessed_letters)
        guess = input("\nPlease select a letter:\n").lower()

        if len(guess) == 1 and guess.isalpha():
            guesses += 1
            if guess in guessed_letters:
                print("\nYou have already guessed the letter", guess)
            elif guess not in secret_random_word:
                print("\nThe letter", guess, "is not in the word.")
                attempts_left -= 1
                guessed_letters.append(guess)
            else:
                print("\nWell done", guess, "is in the word.")
                guessed_letters.append(guess)
                if all(
                    letter in guessed_letters for
                        letter in secret_random_word):
                    guessed = True
                    print("\nCongratulations! You have guessed the word.")
                    update_scoreboard(
                        username, guesses, secret_random_word,
                        guessed_letters)
        else:
            print("Invalid entry. Please enter a single alphabetic character.")

    if attempts_left == 0:
        print(hangman_tries.get_hangman_stage(attempts_left))
        print("Your out of attempts. The word was: ", secret_random_word)

    while True:
        play_again = input("\nDo you want to play again? Y or N\n").lower()
        if play_again == "y":
            clear()
            guesses = 0
            start_game()
            break
        elif play_again == "n":
            print("Thank you for playing Hangman, I hope you enjoyed it!")
            exit()
        else:
            print("Invalid input, please enter Y or N")


def clear():
    """
    This function is to clear the terminal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def start_game():
    """
    This function is called when the user is asked if they
    wish to play again, if they select Y this function will
    be called.
    """    
    welcome()
    secret_random_word = select_random_word(secret_word_list)
    guessed_letters = []
    print(f"The secret word has been chosen for you {username}. Lets play!")
    guess_the_letter(username, guessed_letters, secret_random_word)


if __name__ == "__main__":
    main_page()
    start_game()
