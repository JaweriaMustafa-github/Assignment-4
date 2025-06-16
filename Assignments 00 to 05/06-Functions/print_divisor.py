def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(1, num + 1):  # From 1 to num inclusive
        if num % i == 0:
            print(i)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

# Required to call the main function
if __name__ == '__main__':
    main()
