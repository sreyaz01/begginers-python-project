#  (🪨📜✂️)
import random

# Define Constant,  Upper Case naming convention
ROCK = "r"
PAPER = "p"
SCISSORS = "s"

emojis = {ROCK: "🪨", PAPER: "📜", SCISSORS: "✂️"}
choices = tuple(emojis.keys())  # using Tuple because of it's immutable property


def receive_user_choice():
    while True:
        user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Please enter valid choice!")


def display_inputs(user_choice, comp_choice):
    print(f"You Chose : {emojis[user_choice]}")
    print(f"Computer Chose : {emojis[comp_choice]}")


def winner_announcement(user_choice, comp_choice):
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
        (user_choice == PAPER and comp_choice == ROCK)
        or (user_choice == PAPER and comp_choice == SCISSORS)
        or (user_choice == SCISSORS and comp_choice == ROCK)
    ):
        print("Congratulation! You Win!")
    else:
        print("You lose!")


def play():
    while True:
        user_choice = receive_user_choice()
        #  let computer make a Choice
        comp_choice = random.choice(choices)
        display_inputs(user_choice, comp_choice)
        winner_announcement(user_choice, comp_choice)

        #  Ask The user if the want to continue
        play_again = input(("Wanna play again? (y/n): ")).lower()
        if play_again == "n":
            print("Thanks for playing!")
            break


play()

# TODO
# limit game round to 3 and calculate score in every round print scores and announce winner based on score.
# print continue play option after the announcement of winner.
# reset score after continue and Repeat the process.
