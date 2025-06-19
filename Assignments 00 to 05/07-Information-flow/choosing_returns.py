ADULT_AGE : int = 18 # US adult age

def is_adult(age: int):
    if age >= ADULT_AGE:
        return "Adult"
    return "Minor"

def main():
    age = int(input("How old are you? : "))
    print(is_adult(age))
    
if __name__ == '__main__':
    main()