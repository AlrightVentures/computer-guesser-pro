# Saturday fun - computerGuesserPro
# Similar to numberGuesserPro except now the computer will be guessing the number instead of the user


# Import libraries, modules
import random 


# Define a function where it is computer guessing number  with 'num' function parameter used as a top of the range
def computerGuess(num):

    # Set a range for number picking
    lowestNumber = 1
    highestNumber = num

    # Keep track of the number of tries
    tryCount = 0

    # User will provide the feedback to the computer stating if the number selected it too high or too low
    userResponse = ""

    # Run a while loop until the correct number is picked 
    while userResponse != "C": 

        # Increase tryCounter by 1
        tryCount += 1

        computerPick = random.randint(lowestNumber, highestNumber)
        print(f"Computer picked {computerPick}")
        # User to respond telling computer if the number it picked is too high or too low
        userResponse = input("Type 'H' if the number is higher, 'L' if it's lower, or 'C' if it's correct.\n").upper()

        # Adjust the range from the computer to pick from based on user's feedback
        if userResponse == 'L': 
            highestNumber =  computerPick - 1
        elif userResponse == 'H':
            lowestNumber = computerPick + 1


    print(f"Well done to your computer! It guessed your number {computerPick} correctly.")
    print("It took your computer 1 time." if tryCount == 1 else f"It took your computer {tryCount} times.\n")


# Play the game with a selected number as top of the range, e.g. 5
computerGuess(5)

# Made with love.
# Check out Harry Mack on YouTube. 
# Have a great day.