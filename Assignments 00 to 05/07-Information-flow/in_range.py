def in_range(n: int, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return "Inclusive"
    
    return "Not Inclusive"

def main():
    n = int(input("Enter a number: "))
    low = 0
    high = 100

    print(in_range(n, low, high))

if __name__ == '__main__':
    main() 