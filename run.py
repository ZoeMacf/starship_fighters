"""Module providing randint function from random."""
from random import randint
import os
# create a dictionary to convert letters to numbers,
# allowing user to use Int values to guess ship location
letter_to_number = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

# Uses list comprehension to create a blank list eight times,
# this can then be populated by the user's guesses
# and compared to the ship locations
GUESS_BOARD = [["O"] * 5 for x in range(5)]

# Uses list comprehension to create a blank list eight times,
# this can then be populated by the ships locations
SHIP_LOCATION = [[""] * 5 for x in range(5)]

USER_SHIPS = [["O"] * 5 for x in range(5)]

user_turn = 0
user_score = 0

comp_turn = 0
comp_score = 0


# https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def cls():
    """
    Sends the command 'cls' to the terminal to clear text,
    this will make for better readability for the user throughout the game
    """
    os.system("cls" if os.name == "nt" else "clear")


def start_screen():
    """Prints welcome screen with ASCII art and menu page"""

    print(
        """


                         _____ __                  __    _              
                        / ___// /_____ ___________/ /_  (_)___          
                        \__ \/ __/ __ `/ ___/ ___/ __ \/ / __ \         
                       ___/ / /_/ /_/ / /  (__  ) / / / / /_/ /         
     _________________/____/\__/\__,_/_/  /____/_/ /_/_/ .___/          
    /_____/_____/_____/___       __    __             /_/               
                  / ____(_)___ _/ /_  / /____  __________               
                 / /_  / / __ `/ __ \/ __/ _ \/ ___/ ___/               
                / __/ / / /_/ / / / / /_/  __/ /  (__  )                
               /_/   /_/\__, /_/ /_/\__/\___/_/  /____/_________________
                       /____/                        /_____/_____/_____/
                                                                  
                .                                            .
     *   .                  .              .        .   *          .
  .         .                     .       .           .      .        .
        o                             .                   .
         .              .                  .           .
          0     .
                 .          .                 ,                ,    ,
 .          \          .                         .
      .      \   ,
   .          o     .                 .                   .            .
     .         \                 ,             .                .
               #\##\#      .                              .        .
             #  #O##\###                .                        .
   .        #*#  #\##\###                       .                     ,
        .   ##*#  #\##\##               .                     .
      .      ##*#  #o##\#         .                             ,       .
          .     *#  #\#     .                    .             .          ,
                      \          .                         .
____^/\___^--____/\____O______________/\/\---/\___________---______________
   /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                         --  __     
  
"""
    )

    print("Greetings rookie!\n")
    print("It's time to take to the stars,\
    are you ready to take down the enemy?\n")

    print("1. Start Game\n")
    print("2. Rules\n")
    print("3. Exit Game\n")

    menu_choice = input("Please choose one of the above,\
    using the numbers 1, 2 or 3\n")

    # Check user input and play the next appropriate part of the program.
    if menu_choice == "1":
        begin_game()
    elif menu_choice == "2":
        display_rules()
    elif menu_choice == "3":
        exit_game()
    else:
        print("Please choose something else")


def exit_game():
    """
    Will print a goodbye message to the user and clear the screen"
    """
    while True:
        print("So long rookie!..")
        cls()
        print("Please click Run Program to run again!")
        break


def display_game_board(guess_board, user_board):
    """
    Generates a game board for the user's guess and one with their ships.
    and will then prompt the user to make their first choice
    """
    # Creates a grid for the game_board using join to print
    # row headers and the zip function to pair letters with each row.
    # https://stackoverflow.com/questions/53446425/creating-a-row-of-numbers-letters-in-my-python-battleship-game
    print()
    print("Use this to pinpoint the enemies coordinates\n")
    print()
    print(" ", " ".join("ABCDE"))
    for letter, row in zip("12345", guess_board):
        print(letter, " ".join(row))

    print()
    print("Our forces are ready to go!\n")
    print()
    print(" ", " ".join("ABCDE"))
    for letter, row in zip("12345", user_board):
        print(letter, " ".join(row))


def display_rules():
    """
    Displays the game rules to user and
    allows user to go back to the main menu.
    """

    print(
        "Your goal is to try and take down all\
        of the enemies starships before yours\n"
    )
    print("The starships will be placed around the grid\n")
    print("You must use column and row numbers only to make your guess\n")
    print("If your guess is correct 'HIT' will be displayed to the screen\n")
    print("if not then 'MISS' will be displayed\n")

    print("Can you take out the enemy before they get you?\n")
    print("First to five wins!\n")

    main_menu = input("Type 'return' to go back to the main menu\n")

    if main_menu == "return":
        start_screen()
    else:
        print("Error: Please type 'return' to go back to the main menu")


def create_battleships(game_board):
    """
    Creates 5 ships with random coordinates,\
    these will be then used to populate a hidden
    board for the computer and the user's board.
    """
    # For each of the 5 ships assign a random integer between 1 and 7 to
    # the grid row and column.
    # Add this value to the game_board and assign it 'S'
    for x in range(5):
        battleship_row = randint(0, 4)
        battleship_col = randint(0, 4)
        game_board[battleship_row][battleship_col] = "S"


def user_guess(guess_board, user_board, comp_board):
    """
    Allows the user to guess the location of the ships,
    will then validate both inputs from the user
    after this it will check the user's input against
    the hidden ships and update the grid accordingly.
    """
    # global user_turn
    global user_score
    while True:
        while True:
            try:
                row = int(input("Please enter a row number from 1-5\n")) - 1
                if row not in range(5):
                    raise ValueError("Please enter a value from 1-5")
            except ValueError as e:
                print(f"Invalid value {e}: Please lock\
                in a row coordinate from 1-5\n")
                continue
            else:
                break

        while True:
            try:
                col = (
                    letter_to_number[
                        input("Please enter a column\
                        letter from A-E\n").upper()
                    ]
                    - 1
                )
                if col not in range(5):
                    raise KeyError("Please enter a value from A-E")
            except KeyError as e:
                print(
                    f"Invalid value {e}: Please lock in\
                    a column coordinate from A-E\n"
                )
                continue
            else:
                break

        if comp_board[row][col] == "S":
            guess_board[row][col] = "X"
            # user_turn += 1
            user_score += 1
            cls()
            print("Locking on...\n")
            print("Hit!\n")
            break

        elif guess_board[row][col] == "X":
            # user_turn += 1
            cls()
            print("Hey rookie we fired there already!\n")
            break

        else:
            guess_board[row][col] = "/"
            # user_turn += 1
            cls()
            print("Locking on...\n")
            print("Miss!\n")
            break

    display_game_board(guess_board, user_board)
    if user_score < 5:
        comp_guess(GUESS_BOARD, USER_SHIPS)

    return user_score


def comp_guess(guess_board, user_board):
    """
    Will randomly generate guesses for the\
    computer to try and hit the user's ships
    """
    # global comp_turn
    global comp_score

    print("The enemy has there sights on us!..\n")
    print()
    while True:
        row = randint(0, 4)
        col = randint(0, 4)

        if user_board[row][col] == "S":
            user_board[row][col] = "X"
            comp_score += 1
            cls()

            print("Woah we've been hit!\n")
            break
        else:
            user_board[row][col] = "/"
            cls()

            print("Hah! Thought you could hit us!\n")
            break

    display_game_board(guess_board, user_board)

    return comp_score


# Code credit on play_game function
# goes to Joanne Lee: https://github.com/lee-joanne/pirate_ship/tree/main
def play_game():
    """
    Will create a loop to continuously play
    the game until either the user or computer
    reaches a score of 5, once score is met
    a win or lose message is printed.
    """
    while True:
        user_guess(GUESS_BOARD, USER_SHIPS, SHIP_LOCATION)
        if user_score == 5:
            print("You did it! Guess you're not a rookie anymore!\n")
            print("To play again please hit 'Run Program' at the top\n")
        elif comp_score == 5:
            print("Well that didn't go as planned,\
            back to training for you!\n")
            print("To play again please hit 'Run Program' at the top\n")
        else:
            pass


def begin_game():
    """
    Will create the ships for both the user's
    board and the computer's hidden ships board
    once done the user's board and a blank
    board for guessing will be displayed.
    Finally the game will be played out.
    """
    create_battleships(SHIP_LOCATION)
    create_battleships(USER_SHIPS)
    display_game_board(GUESS_BOARD, USER_SHIPS)
    play_game()


if __name__ == "__main__":
    start_screen()
