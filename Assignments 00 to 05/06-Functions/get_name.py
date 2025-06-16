def get_name():
    # Ask the user to type their name
    return input("Please enter your name: ")


def main():
    name = get_name()  # This gets the user's name from the function
    print("Howdy", name, "! 🤠")

if __name__ == '__main__':
    main()
