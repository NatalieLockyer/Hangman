# To randomise words and to add stages of the hangman one a life is lost
import random

# Access to hangman_tries.py
import hangman_tries

# Access to the list of words 
from words import secret_word_list

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
    print("<>  <>   <><>   <>    <>   <>>>>  <>      <>   <><>  <>    <>")
    print("<>  >>  <>  <>  <>>   <>  <>      <><>  <><>  <>  <> <>>   <>")
    print("<><><>  <><><>  <> <> <>  <>      <>  <>  <>  <><><> <> <> <>")
    print("<>  <>  <>  <>  <>   <<>  <>  >>> <>      <>  <>  <> <>   <<>")
    print("<>  <>  <>  <>  <>    <>   <<<<   <>      <>  <>  <> <>    <>")

    print("--------------------------------------------------------------")
    print("--------------------------------------------------------------")

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
        guess = input("Please select a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed the letter", guess)
            elif guess not in secret_random_word:
                print("The letter", guess, "is not in the word.")
                attempts_left -= 1
                guessed_letters.append(guess)
            else:
                print("Well done", guess, "is in the word.")
                guessed_letters.append(guess)
                if all (letter in guessed_letters for letter in secret_random_word):
                    guessed = True
                    print("Congratulations! You have guessed the word correctly.")

        else:
            print("Invalid entry. Please enter a single alphabetic charactor.")
    
    if attempts_left == 0:
        print(hangman_tries.get_hangman_stage(attempts_left))
        end_game = True
        print("Unfortunately, you have run out of attempts. The word was: ",secret_random_word)


    while True:
        play_again = input("Do you want to play again? Y or N ").lower()
        if play_again not in ["y", "n"]:
            print("Invalid input, please enter Y or N")
        elif play_again == "y":
            start_game()
        else: 
            print("Thank you for playing Hangman, I hope you enjoyed it!")
        


def start_game():
    """
    """
    player_name = welcome()
    secret_random_word = select_random_word(secret_word_list)
    guessed_letters = []
    print(f"The secret word has been chosen for you {player_name}. Lets play!")
    guess_the_letter(guessed_letters, secret_random_word)

if __name__ == "__main__":
    start_game()