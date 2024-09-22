import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the number between 1 to 100: "))
        if guess > number_to_guess:
            print("Too high!")
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Congratulation, You guessed it right.")
            break
    except ValueError:
        print("Please enter a valid number")

# TODO
# ask do you wanna play again
# if y repeat game
# if n
# print greeting massage
