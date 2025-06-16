def average(num1:float , num2:float):
    sum = num1 + num2
    return sum / 2

def main():
    # Ask the user to enter two numbers
    No_1 = input(float("Enter the first number: "))
    No_2 = input(float("Enter the second number: "))

    # Call the average function and print the result
    result = average(No_1, No_2)
    print("The average is:" , result)

if __name__ == '__main__' :
    main()