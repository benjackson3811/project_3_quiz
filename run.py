# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import sys
import os
import time
import random
from quiz_questions import questions
from quiz_questions import answers
from quiz_questions import options


def start_menu():
    """
    function to show the user the menu options avaliable to them.

    """
    print()
    print()
    print("-----------------------------")
    print()
    print("Welcome to the Cape Town Quiz")
    print()
    print("-----------------------------")
    print()
    time.sleep(2)
    clear_screen()
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
        start_menu()
    elif selection == "3":
        sys.exit
        clear_screen()
    else:
        clear_screen()
        print("Invalid Selection - please select one of the the three options")
        return start_menu()
# -------------------


def game_instructions():
    """
    game instructions for the user
    """
    print(" You will answer five questions!")
    print()
    print(" They will be a mixture of three topics")
    print()
    print(" 1: Cape Town History")
    print(" 2: The Sea. ")
    print(" 3: South African Land Answers")
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
    new_questions, new_answers, new_options = zip(*temp_list)
    new_questions, new_answers, new_options = list(new_questions), list(new_answers), list(new_options)

    for index, question in enumerate(new_questions):
        print("-------------------")
        print(question)
        for option in new_options[question_num-1]:
            print(option)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(new_answers[index], guess)
        question_num += 1
        if question_num == 6:
            break
        time.sleep(1)
        clear_screen()

    display_score(correct_guesses, guesses)

# -------------------


def check_answer(new_answer, guess):
    if new_answer == guess:
        print("⭐ Correct! ⭐!")
        return 1
    else:
        print("Wrong! The correct answer is " + str(new_answer))
        return 0


# -------------------
def display_score(correct_guesses, answers):
    print("Calculating the score!")
    print("-------------------")
    print("The results!")
    print()
    score = int((correct_guesses/len(answers))*100)
    print("Your score is: "+str(score)+"%")
    print("-------------------")


# -------------------
def play_again():
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
    start_menu()

    while play_again():
        new_game()

    print("Thanks for playing!!!")


front_screen()
