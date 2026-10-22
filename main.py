from wordle_functions import (
    choose_word,
    get_guess,
    evaluate_guess,
    display_guess,
    has_won
)


def main():
    print("Welcome to Mystery Wordle!")
    print("Guess the five-letter word.")
    print("G = correct letter and position")
    print("Y = correct letter, wrong position")
    print("- = no remaining match for that letter")
    print()

    play_again = "yes"

    while play_again in ["yes", "y"]:
        # Reset the game for each new round.
        secret_word = choose_word()
        previous_guesses = []
        maximum_attempts = 6
        player_won = False

        for attempt in range(1, maximum_attempts + 1):
            print("Attempt", attempt, "of", maximum_attempts)

            # Invalid or repeated guesses do not use an attempt.
            guess = get_guess(previous_guesses)
            previous_guesses.append(guess)

            feedback = evaluate_guess(guess, secret_word)
            display_guess(guess, feedback)

            if has_won(guess, secret_word):
                player_won = True
                print("Congratulations! You solved the puzzle.")
                break

        if not player_won:
            print("You have used all six attempts.")
            print("The secret word was:", secret_word)

        # Require a clear yes or no before continuing.
        play_again = input(
            "Would you like to play again? (yes/no): "
        ).strip().lower()

        while play_again not in ["yes", "y", "no", "n"]:
            play_again = input(
                "Please enter yes or no: "
            ).strip().lower()

        print()

    print("Thanks for playing!")


# Start the game when this file is run directly.
if __name__ == "__main__":
    main()