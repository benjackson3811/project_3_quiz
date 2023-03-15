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


def display_menu():
    """
    function to show the user the menu options avaliable to them.

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
        display_menu()
    elif selection == "3":
        sys.exit
    else:
        clear_screen()
        print("Invalid Selection - please select one of the the three options")
        return display_menu()
# -------------------


def game_instructions():
    """
    game instructions for the user
    """
    print("There are three quiz topics you can asnwer questions on")
    print(" 1: Cape Town History")
    print(" 2: The Sea. ")
    print(" South African Land Answers")
    print(" For each topic, there are 5 multiple choice questions.")
    print(" You have four options, A, B, C or D")
    print(" If your answer is correct, the system will tell you!")
    print()
    print(" Press any button to go back to the main screen")
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
        if (question_num == 5):
            break

    display_score(correct_guesses, guesses)
# -------------------


def check_answer(answer, guess):
    if answer == guess:
        print("⭐ Correct! ⭐!")
        return 1
    else:
        print("Wrong! The correct answer is " + str(answer))
        return 0


# -------------------
def display_score(correct_guesses, guesses):
    print("-------------------")
    print("Results")
    print()
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")
    print("-------------------")


# -------------------
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    lower_response = response.lower()

    if lower_response == "yes":  # Change "yes" to lower as well
        return True
    else:
        return False
# -------------------


def front_screen():
    """shows the display menu function options for the user"""
    print("-----------------------------")
    print()
    print()
    print("Welcome to the Cape Town Quiz")
    print()
    print()
    print("-----------------------------")
    clear_screen()
    time.sleep(2)
    print()
    print()
    display_menu()

    while play_again():
        new_game()

    print("Thanks for playing!!!")


front_screen()
