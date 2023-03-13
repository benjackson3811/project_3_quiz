# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


# -------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# -------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong! The answer is "+str(answer))
        return 0


# -------------------
def display_score(correct_guesses, guesses):
    print("-------------------")
    print("Results")
    print("-------------------")
    print('Answers: ', end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print('Guesses: ', end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


# -------------------
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "Yes":
        return True
    else:
        return False
# -------------------


questions = {
    "What other name is Cape Town known as?: ": "A. Mother City",
    "Which provenice is the city located?: ": "A. Western Cape",
    "What year was the city founded?: ": "C. 1652",
    "What Language is is majorly used in the city?: ": "D. English",
    "Which of these was instrutmental in the creation of the city?: ":
    "D. Dutch East India Company"
}

options = [["A. Mother City", "B. New City", "C. Kaap Stad", "D. The City!"],
    ["A. Western Cape", "B. Cape Fear", "C. Cape Beer ", "D. Africa"],
    ["A. 1625", "B. 1642", "C. 1652", "D. 1632"],
    ["A. Bandu", "B. Xhorsa", "C. Afikaans", "D. English"],
    ["A. HSBC", "B. Coke", "C. Gap", "D. Dutch East India Company"]]

new_game()

while play_again():
    new_game()

print("Byyeee!!!")
