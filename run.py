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
print(f"Welcome to Hangman {username}, lets get started!")

def get_word(secret_word_list):
    """
    This function returns a random word from secret_word_list
    """
    return random.choice(secret_word_list)



# def play_game(get_word)
# secret_word = " _ " * len()

print(get_word(secret_word_list))

