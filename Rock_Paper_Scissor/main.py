import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock, paper, scissors]

user_choice = int(input("Choose. 0=Rock, 1=Paper, 2=Scissors \n"))
print(game_image[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose: ")
print(game_image[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice >= 3 or user_choice < 0:
    print("Please input 0, 1 or 2")
elif computer_choice > user_choice:
    print("Computer wins")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice == user_choice:
    print("Draw!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")


