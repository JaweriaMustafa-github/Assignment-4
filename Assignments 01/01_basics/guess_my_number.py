import random

def play_game():
    # Generate a random secret number between 1 and 99
    secret_number = random.randint(1, 99)
    print("\nI am thinking of a number between 1 and 99...")

    attempts = 0

    while True:
        try:
            guess = int(input("Enter a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Your guess is too low\n")
            elif guess > secret_number:
                print("Your guess is too high\n")
            else:
                print(f"🎉 Congrats! The number was: {secret_number}")
                print(f"You guessed it in {attempts} tries.")
                break

        except ValueError:
            print("❗ Please enter a valid number!\n")

def main():
    while True:
        play_game()

        # Ask the user if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! 👋")
            break

# Required line to run the main function
if __name__ == '__main__':
    main()
