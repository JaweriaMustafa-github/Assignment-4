def main():
    curr_value = int(input("Enter a number: "))
    curr_value = curr_value * 2  # First doubling before the loop
    
    while curr_value < 100:
        print(curr_value)
        curr_value = curr_value * 2
    
    print(curr_value)  # Also print the final doubled value which is >= 100

if __name__ == '__main__':
    main()
