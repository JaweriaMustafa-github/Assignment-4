def main():
    # Ask the user to enter a number and convert it to integer
    curr_value = int(input("Enter a number: "))
    
    # Double the number until it's 100 or greater
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

# This provided line is required at the end of the file
if __name__ == '__main__':
    main()
