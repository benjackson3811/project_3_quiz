# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import os
import random
import time
from quiz_questions import questions
from quiz_questions import answers
from quiz_questions import options


def game_start():
    """
    Start Menu Function
    """
    print()
    print("      -----------------------------")
    print()
    print("      Welcome to the Cape Town Quiz")
    print()
    print("      -----------------------------")
    print()
    game_navigation()
# -------------------


def game_navigation():
    """
    Game navigation functions to show directly after the game_start function.
    Function purpose is to provide the user with three choices.
    1) play the game straight away.
    2) Instructions
    3) Quit the game
    """
    time.sleep(2)

    selection = input("""


    -----------------------------
    1: Start Quiz
    2: Game Instructions
    3: Quit Game
    -----------------------------
    Please enter a choice
    1, 2 or 3
    -----------------------------

    """)
    if selection == "1":
        clear_screen()
        new_game()
    elif selection == "2":
        clear_screen()
        game_instructions()
        game_navigation()
    elif selection == "3":
        clear_screen()
    else:
        print("Invalid Selection - please select one of the the three options")
        return game_navigation()
# -------------------


def game_instructions():
    """
    How to play the game instructions for the user
    """
    print(" You will answer eight questions!")
    print()
    print(" The topic of the questions will be Cape Town!")
    print()
    print(" Each question has four options, A, B, C or D")
    print()
    print(" If your answer is correct, you can answer the next question")
    print()
    print(" If the answer is incorrect, the system will tell you!")
    print()
    input("Press any button to go back to the main screen.  ")
    clear_screen()
# -------------------


def clear_screen():
    """
    function to clear screen
    """
    os.system('clear')


# -------------------
def new_game():
    """
    function to load up the game, define the questions to be asked
    """
    guesses = []
    correct_guesses = 0
    question_num = 1
    temp_list = list(zip(questions, answers, options))
    random.shuffle(temp_list)
    new_qst, new_ans, new_opt = zip(*temp_list)
    new_qst, new_ans, new_opt = list(new_qst), list(new_ans), list(new_opt)

    for index, question in enumerate(new_qst):
        print("-------------------")
        print(question)
        for option in new_opt[question_num-1]:
            print(option)
        guess = guess_input()
        guess_validation(guess)
        guesses.append(guess)
        correct_guesses += check_answer(new_ans[index], guess)
        question_num += 1
        if question_num == 11:
            break

    display_score(correct_guesses, guesses)
# -------------------


def guess_input():
    """
    Function purpose:  to recieved the inputted guess.
    Function set up: a while loop.
    Guess = varible.
    variable passed and checked in guess validate() validated
     to make sure the guess is A,B,C,D
    """
    while True:
        guess_try = input("Enter (A, B, C, or D):\n ")
        guess = guess_try

        if guess_validation(guess):
            break
    return guess
# -------------------


def guess_validation(guess_try):
    """
    Function purpose: Validate the guess input to ensure only
    A,B,C,D answers are given
    Function set up:
    if input == (A, B, C, or D) this is invalid - no error will show.
    if input != (A, B, C, or D - error shown and user will have to answer again
    """
    if guess_try not in ['A', 'B', 'C', 'D']:
        print("Stop! ⛔ Error - invalid.")
        print("Please enter [A, B , C, or D only")
        return False
    else:
        return True
# -------------------


def check_answer(new_ans, guess):
    """
    function purpose: to check the answer given to the question
    function set up: if statement to check the guess = answer
    """
    if new_ans == guess:
        print("⭐ Correct! ⭐!")
        return 1
    else:
        print("⛔ Wrong! The correct answer is " + str(new_ans))
        return 0


# -------------------
def display_score(correct_guesses, new_ans):
    """
    function purpose: to show the user % score of the questions answered
    function set up: math element dividing the correct guesses by the answers
    """
    print("Calculating the score!")
    print("-------------------")
    print("The results!")
    print()
    score = int((correct_guesses/len(new_ans))*100)
    print("Your score is: "+str(score)+"%")
    print("-------------------")


# -------------------
def play_again():
    """
    Funciton purpose: to provide the option to play again
    Function set up:
    If/ elif statement - three options
    1) new game
    2) exits game
    3) validates the response to ensure correct response given.
    """
    print("How about another game? ")
    response = input("Do you want to play again? (YES or NO): ")
    response = response.upper()

    if response == "YES":
        game_navigation()
    elif response == "NO":
        clear_screen()
        print("Thanks for playing the game")
    elif response not in {response == "YES", response == "NO"}:
        play_again()
# -------------------


def front_screen():
    """
    function purpose: to archor the game -
    shows the display menu function options for the user
    set up - a while statement
    """
    game_start()

    while play_again():
        game_navigation()

    print("Thanks for playing!!!")


front_screen()
