import random


def get_upper_limit(low):
    """Prompt the user for a valid upper limit.
    Ensure the lower limit is less than the upper limit."""

    while True:
        try:
            high = int(input("Please provide the higher limit: "))
            while low >= high:
                high = int(
                    input(
                        "Please provide a higher limit correctly! 😄 (default lower is set to 1): "
                    )
                )
            return high
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def get_feedback(comp_guess):
    """Prompt the user for feedback on the computer's guess."""
    return input(
        f"Is {comp_guess}, too high (H), too low (L), or correct (C)? "
    ).lower()


def update_limits(feedback, comp_guess, low, high):
    """Update the guessing range based on user feedback."""
    if feedback == "l":
        low = comp_guess + 1  # Adjust the lower limit
    elif feedback == "h":
        high = comp_guess - 1  # Adjust the upper limit
    return low, high


def make_guess(low, high):
    """Generate a new guess within the current limits."""
    return random.randint(low, high)


def main():
    low = 1
    choices = ("c", "h", "l")

    # Get the upper limit from the user
    high = get_upper_limit(low)

    # Initial computer guess
    comp_guess = make_guess(low, high)

    while True:
        feedback = get_feedback(comp_guess)

        if feedback in choices:
            if feedback == "c":
                print(f"Yay! The computer guessed the number, {comp_guess}, correctly!")
                break

            # Update limits based on feedback
            low, high = update_limits(feedback, comp_guess, low, high)

            # Ensure valid range for guessing
            if low >= high:
                print("It seems there are no valid numbers left to guess!")
                break

            # Generate a new guess
            comp_guess = make_guess(low, high)
        else:
            print("Please enter a valid choice: C, H, or L.")


main()
