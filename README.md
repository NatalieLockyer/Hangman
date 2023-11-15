# [Hangman Game](https://hang-man2023-457c30e677c0.herokuapp.com/)
(Developer: Natalie Lockyer)

Hang Man is a word guessing game, based on the original 'Hangman'. The game has been designed to give users a limited number of lives to guess the secret word. The secret word is displayed as underscores ( _ _ _ ) .When a player guesses the letter correctly, the letter appears in the word which is displayed under the diagram. If they guess the letter in correctly, a life will be lost and a part of the stick man will dispaly on the diagram. Once the game has finished users will be given the oppurtunity to play again.

## Demo
[To view live website, click here](https://hang-man2023-457c30e677c0.herokuapp.com/)

<p align="center">
<img src="./assets/images/readme_imgs/main_page.png">
</p>


# Contents
+ [User Experience](#user-experience)
    + [Key Project Goals](#key-project-goals)
    + [Target Audience](#target-audience)
    + [User Requirements and Expectations](#user-requirements-and-expectations)
    + [User Stories](#user-stories)
    + [Lucid Chart](#lucid-chart)
+ [Design ]
    + [Typography ](#typography)
+ [Features ]
     + [Main Start Page ](#main-start-page)
     + [Game Instructions Page ](#game-instructions-page)
     + [Scoreboard Page ](#scoreboard-page)
     + [Exit Page ](#exit-page)
     + [Start New Game Page ](#start-new-game-page)
     + [Lose Screen Page ](#lose-screen-page)
     + [Win Screen Page ](#win-screen-page)
     + [Goodbye Page ](#goodbye-page)
     + [Future Features](#future-features)
  + [Technologies Used]
    + [Languages Used]
    + [Frameworks Used]
+ [Testing ]
  + [Validator Testing]
  + [Lighthouse Testing]
  + [Problems Encountered]
  + [Responsiveness ]
  + [Full Testing ]
 + [Deployment and Local Deployment]
  + [Deployment ]
  + [Local Deployment]
  + [How to Clone]
+ [Credits ]
  + [Code ]
  + [Media ]
  + [Acknowledgements ]

***
***

# User Experience

### Key Project Goals
* To write and develop an enjoyable interactive game in a terminal in Python.
* The functionality of the game should keep to the core concepts of Hangman.
* The user should be able to navigate around this easily. 
* On the loading screen, the user is able to choose options to either, start the game, read the game instructions, view the scoreboard, or exit the game. 
* Add username and amount of guesses taken to google sheets so the score board is updated.
* At the end of the game the user is able to choose if they wish to play again, or exit the game.

### Target Audience
  * Users of any age that would like to play an enjoyable and interactive word game. 
  * Users who wish to improve thier spelling skills, increase vocabulary and keep the mind focused.  
  * Users who like terminal based games.

### User Requirements and Expectations 
  * An accessible game that is clear and easy to understand.
  * The ability to personalise the game by adding your name.
  * A fun and interactive game that is appealing and well structured and has clear navigation options.
  * Users are able to find instructions on how to play if they are not familiar with the game, and given the time they need to read this.
  * To be able to view the scoreboard, which is linked to google sheets to see the list of how many guesses it has taken them and other users.
  * Users to recieve feedback throughout the game, whether this is that they have dulplicated a letter, the user has won or the user has lost the game. 
  * Users are able to select Y or N if they wish to play again. If no the player will be taken back to the main menu. 
    
### User Stories
As a site visitor,

  * I want to play interactive game.
  * Initially a red button with run program and a large black screen underneath appear.
  * When the run program button is selected I can see the title 'Hangman'.
  * I am given 4 choices of what I would like to do, 
    + 1 - Start Game
    + 2 - Game Instructions
    + 3 - Scoreboard
    + 4 - Exit Game
  * I start with 1, When I enter 1, I am asked for my name, Once I enter this I am taken to a new screen where I can see the hang man stand and a number of underscores relating to the secret word. 
  * I guess a letter and its correct. The letter replaces the underscore in the word and I can guess another letter.
  * I duplicate this letter and recieve a message explaining that I have already used this letter.
  * I guess another letter incorrectly and a life is lost. This appears on the hang man diagram.
  * Once I have used up all my lives, I recieve a message telling me as such. I am then asked if I want to play again (Y or N), I click Y, this asks me for my name again and the game will restart on a new screen.
  * Once I guess all the letters correctly, I receive a messageg telling me as such. I am then asked if I wish to play again this time I select N and I return to the main menu. 
  * I would like to see how many guesses it took to win on the previous game. I press 3 on the main page and this takes me onto a new page called Score Board. I can see how many guesses this last game took me and I can see other users game information too. I then press ENTER to return to the main menu.
  * I then select option 2, this takes me to a new screen and shows me the 'rules' of the game. Once I have read them I click ENTER and I am taken back to the main page.
  * I then select option 4, this exits me out of the game.

### Lucid Chart
I have created this flow chart diagram on Lucid Charts. This was used to help with writing the game functionality. 

<p align="center">
<img src="./assets/images/readme_imgs/lucid_chart.jpeg">
</p>

## Design

## Typography

For the main titles on the page, I used Figlet. I initally chose a font called 'acrobatic' which was letter made up from small stick figures. When I ran this in the terminal, the font was far to big. I wasnt able to reduce the size of the font. 
I then opted for a font called 'Banner', the titles now sit nicely on the page. I have also centered them using justify-centre.
This image was extracted from the [Figlet webpage](www.figlet.org/examples)

<p align="center">
<img src="./assets/images/readme_imgs/figlet_font.png">
</p>

## Features

### Main Start Page

This is the main screen page. Here you can see the title of the game and a welcome message. There is also a main menu where the user can choose 1 of 4 options. 
1 to start a New Game, 2 for the Game Instructions, 3 for the scoreboard and 4 to exit the game. 
The user is able to chose which option by selecting one of these numbers from thier keypad.

<p align="center">
<img src="./assets/images/readme_imgs/main_page.png">
</p>

### Game Instructions Page

When the user selections option 2, they will see a new screen with the game instuctions. Once the user has finished with this they can hit enter to return to the main screen. 

<p align="center">
<img src="./assets/images/readme_imgs/game_instructions.png">
</p>

### Scoreboard Page

When the user selections option 3, they will see a new screen with the scoreboard. This is updated when a player completes a winning game. The user can also see the scores of other players and the scores are in acending order.

<p align="center">
<img src="./assets/images/readme_imgs/score_board.png">
</p>

Updated Page - The scoreboard is updated with any winning games.

<p align="center">
<img src="./assets/images/readme_imgs/updated_scoreboard.png">
</p>

### Exit Page

If the user does not wish to play the game at all, they can simple select option 4 which will exit the game, there is a confirmation message saying "Goodbye".

<p align="center">
<img src="./assets/images/readme_imgs/exit_mainpage.png">
</p>

### Start New Game Page

To start a new game, the user selects option 1. The user is then asked to enter their name. The name that they enter here will be used in the welcome message. 

<p align="center">
<img src="./assets/images/readme_imgs/new_game.png">
</p>

If the user does not enter anything, they will see a message "You havent entered anything...Please enter your name!"

<p align="center">
<img src="./assets/images/readme_imgs/no_name.png">
</p>

Once the user, confirms their name by pressing the enter key, the game will begin on a new screen. The page displays a welcome message with the users name, it explains that a new secret word has been chosen and to begin you must select a letter. The empty hangman stand is also on the screen.

<p align="center">
<img src="./assets/images/readme_imgs/ng_img1.png">
</p>

The user enters a letter, if this is not an alphabetic letter, a message will appear telling the user that thats an invalid entry and to select a single alpabetic character. If the user selects multiple letters the user will be shown the same message. 

<p align="center">
<img src="./assets/images/readme_imgs/invalid_letter.png">
</p>

If the user enters a letter that is not in the word, a message appears telling the user that the letter they entered is not in the word, and a life will be lost. This is displayed as a head on the hangman stand. For each incorrect letter guessed, the hangman will continue to add body parts, in total there are 6 parts (head, body, 2 legs and 2 arms.) The user then selects another letter. 

<p align="center">
<img src="./assets/images/readme_imgs/ng_img2.png">
</p>

If the user guesses a correct letter, a message will appear telling the user that the letter they entered is in the word and replaces the underscore in the place the letter sits. The user then selects another letter.

<p align="center">
<img src="./assets/images/readme_imgs/ng_img3.png">
</p>

### Lose Screen Page

Once the user has exhausted all their tries they lose the game. The player will see a message explaining that they have lost and will reveal what the secret word was. The user is asked if they would like to play again?

<p align="center">
<img src="./assets/images/readme_imgs/ng_img4.png">
</p>

If the user selects Y to play again, a new screen will appear and a new game will begin. 

<p align="center">
<img src="./assets/images/readme_imgs/ng_img5.png">
</p>

### Win Screen Page

If the user guesses all the letters before the hangman is hung, the game is complete and the users wins. A message is displayed explaining that they have won and would they like to play again.

<p align="center">
<img src="./assets/images/readme_imgs/winning_letter.png">
</p>

### Goodbye Page

If the user chooses not to play again this time, they select N and the game with exit with the message "Thank you for playing, I hope you enjoyed it!"

<p align="center">
<img src="./assets/images/readme_imgs/playagain_no.png">
</p>

### Future Features
In the futures I would like to add the following features:

* I would like to add a frame and colours to make the game look more appealing
* I would like users to be able to create an account so that each time they play on the game they can input their login in details.
* To add a defensive question when a player selects Y to exit, "Are you sure you want to exit Y or N?"

## Technologies Used

### Language
* Python

### Frameworks and Tools

* GitHub
* Gitpod
* Heroku
* Lucid Chart



