import random

Done_Likelihood = 0.3

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return # Stop early if done() returns True
        print (curr_num)

# Helper function to randomly decide whether to stop or not
def done():
    """Returns True with a probability of DONE_LIKELIHOOD"""
    return random.random() < Done_Likelihood

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done!")

if __name__ == '__main__':
    main()