# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import sys
import os
import random
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
        game_navigation()()
    elif selection == "3":
        sys.exit
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
    print(" They will all be on topics on Cape Town")
    print()
    print(" - Cape Town History")
    print(" - The Sea")
    print(" - South African land animals")
    print()
    print(" Each question has four options, A, B, C or D")
    print()
    print(" If your answer is correct, the system will tell you!")
    print()
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
        print("Error - invalid.")
        print("Please enter [A, B , C, or D only")
        return False
    else: 
        return True


# -------------------


def check_answer(new_ans, guess):
    """
    function to check the answer given to the question
    """
    if new_ans == guess:
        print("⭐ Correct! ⭐!")
        return 1
    else:
        print("Wrong! The correct answer is " + str(new_ans))
        return 0


# -------------------
def display_score(correct_guesses, answers):
    """
    function to show the % score of the questions answered
    """
    print("Calculating the score!")
    print("-------------------")
    print("The results!")
    print()
    score = int((correct_guesses/len(answers))*100)
    print("Your score is: "+str(score)+"%")
    print("-------------------")


# -------------------
def play_again():
    """
    function to provide the option to play again
    """
    response = input("Do you want to play again? (yes or no): ")
    lower_response = response.lower()

    if lower_response == "yes":
        return True
    else:
        return False
# -------------------


def front_screen():
    """
    shows the display menu function options for the user
    """
    game_start()

    while play_again():
        game_navigation()()

    print("Thanks for playing!!!")


front_screen()
