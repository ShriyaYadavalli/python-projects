import random

# Rock, Paper, Scissors images
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

# Get valid user choice
while True:
    user_output = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    if user_output == 0:
        print(f"You chose:\n{rock}")
        break
    elif user_output == 1:
        print(f"You chose:\n{paper}")
        break
    elif user_output == 2:
        print(f"You chose:\n{scissors}")
        break
    else:
        print("Invalid choice. Try again.")

# Computer choice
comp_output = random.randint(0, 2)

if comp_output == 0:
    print(f"Computer chose:\n{rock}")
elif comp_output == 1:
    print(f"Computer chose:\n{paper}")
else:
    print(f"Computer chose:\n{scissors}")

# Decide winner
if user_output == comp_output:
    print("It is a tie")
elif (user_output - comp_output) in [-2, 1]:
    print("You win")
else:
    print("You Lose")