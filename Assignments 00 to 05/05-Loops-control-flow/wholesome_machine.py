AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()

    while user_feedback != AFFIRMATION:
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")

# Required to run the program
if __name__ == '__main__':
    main()
