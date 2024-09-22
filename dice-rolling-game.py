import random

while True:
    choice = input("Roll the Dice? (y/n) :  ").lower()
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice == "n":
        print("Thanks for Playing!")
        break
    else:
        print("invalid Choice")

# TODO:
# Modify the Program so that user can specify how many dice they want to roll
# Add a feature that keep s track of how many times the user has rolled the dice during the session
