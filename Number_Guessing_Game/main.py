from random import randint
from art import logo

EASY_TURNS = 10
HARD_TURNS = 5

#Function to check user's guess against answer
def check_answer(user_guess, actual_answer, turns):
    """ Checks guess against answer and shows remaining turns """
    if user_guess > actual_answer:
        print("Too HIGH")
        return turns -1
    elif user_guess < actual_answer:
        print("Too LOW")
        return turns -1
    else:
        print(f"You got it!, the answer is {actual_answer}")

#Function to set difficulty
def check_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

def game():
    #Choosing a random number between 1 & 100
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = check_difficulty()

    #Repeat the guess as a function
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts left. Make a guess quickly")
        #Let the user guess a number of their choice
        guess = int(input("What are you thinking? "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have no guesses left. You LOSE!")
            return
        elif guess != answer:
            print("Guess Again")
game()