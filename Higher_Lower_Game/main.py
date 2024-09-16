import random
from art import logo, vs
from game_data import data

def format_data(account):
    """Takes the account data and returns a readable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}."

def check_answer(user_guess, a_followers, b_followers):
    """Take a users guess and the followers count & returns if they got correct."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers?, A or B: ").lower()
    print("\n" * 20)
    print(logo)
    follower_count_a = account_a["follower_count"]
    follower_count_b = account_b["follower_count"]
    is_correct = check_answer(guess, follower_count_a, follower_count_b)
    if is_correct:
        score += 1
        print(f"You have answered correctly. Currect score is {score}")
    else:
        print(f"Sorry, That was incorrect. Your final score is {score}")
        game_should_continue = False