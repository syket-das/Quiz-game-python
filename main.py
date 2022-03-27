# ------------------------------------
from pygtkcompat import enable_gst


def new_game():
    guesses = []
    currect_guesses = 0
    question_number = 0

    for key in questions:
        print("------------------------------------")
        print(key)

        for i in options[question_number - 1]:
            print(i)
        guess = input("Enter A , B, C or D: ")
        guess = guess.upper()
        guesses.append(guess)

        check_answers(questions.get(key), guess)

        question_number += 1

    display_score(currect_guesses, guesses)


# ------------------------------------


def check_answers(answer, guess):
    if(answer == guess):
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

# ------------------------------------


def display_score(currect_guesses, guesses):
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((currect_guesses / len(questions)) * 100)
    print("Score: ", score, "%")

    play_again()

# ------------------------------------


def play_again():
    print("Do you want to play again? (Y/N)")
    again = input()
    again = again.upper()
    if(again == "Y"):
        new_game()
    else:
        print("Bye!")
        exit()

# ------------------------------------


questions = {
    "What is the capital of France?": "A",
    "What is the capital of Spain?": "D",
    "What is the capital of Italy?": "B",
    "What is the capital of Germany?": "B",
}


options = [
    ["A. Paris", "B. Madrid", "C. Rome", "D. Berlin"],
    ["A. Rome", "B. Berlin", "C. Paris", "D. Madrid"],
    ["A. Berlin", "B. Rome", "C. Madrid", "D. Paris"],
    ["A. Madrid", "B. Berlin", "C. Rome", "D. Paris"]
]

new_game()
