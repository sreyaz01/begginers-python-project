#  (🪨📜✂️)
import random

emojis = {"r": "🪨", "p": "📜", "s": "✂️"}
choices = ("r", "p", "s")  # using Tulip because of it's immutable property
while True:
    user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Please enter valid choice!")
        continue

    #  let computer make a Choice
    comp_choice = random.choice(choices)

    print(f"You Chose : {emojis[user_choice]}")
    print(f"Computer Chose : {emojis[comp_choice]}")

    """
    RULE :
    rock & paper, Paper Wins
    paper & scissor, scissor wins
    scissor & rock,  Rock wins
    """
    # Determine the winner
    if user_choice == comp_choice:
        print("It's a Tie!")
    elif (
        (user_choice == "p" and comp_choice == "r")
        or (user_choice == "p" and comp_choice == "s")
        or (user_choice == "s" and comp_choice == "r")
    ):
        print("Congratulation! You Win!")
    else:
        print("You lose!")

    #  Ask The user if the want to continue
    play_again = input(("Wanna play again? (y/n): ")).lower()
    if play_again == "n":
        print("Thanks for playing!")
        break
