def get_user_numbers():
    """
    Prompts the user to enter numbers until a blank line is entered.
    Returns the list of entered numbers as integers.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        num = int(user_input)
        user_numbers.append(num)
    return user_numbers


def count_nums(num_lst):
    """
    Counts how many times each number appears in the list using a dictionary.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict


def print_counts(num_dict):
    """
    Prints the count of each number from the dictionary.
    """
    for num in num_dict:
        print(f"{num} appears {num_dict[num]} times.")


def main():
    """
    Main function to run the program.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


# Required to run main() only when the script is executed directly
if __name__ == '__main__':
    main()
