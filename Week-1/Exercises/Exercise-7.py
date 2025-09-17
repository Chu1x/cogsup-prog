"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""
# Function to get valid feedback from the user
def input_feedback(prompt):
    feedback = input(prompt).lower()  # Get input and change it to lowercase
    while feedback not in ('h', 'l', 'c'):  # Only accept 'h', 'l', 'c'
        print("Please enter 'h' (too high), 'l' (too low), or 'c' (correct).")
        feedback = input(prompt).lower()
    return feedback

# Initialize search range
low = 1        # Minimum possible number
high = 100     # Maximum possible number
print("Think of a number between 1 and 100. I will try to guess it!")

# Start guessing loop
feedback = ''  # Feedback on current guess
while feedback != 'c':  # Repeat until the computer guesses correctly
    guess = (low+high) // 2  # Computer guesses the middle of the current range
    print(f"My guess is {guess}.")  # Show the guess to the user
    
    # Ask the user whether the guess is too high, too low, or correct
    feedback = input_feedback("Enter 'h' if too high, 'l' if too low, 'c' if correct: ")
    
    if feedback == 'h':
        high = guess - 1  # Adjust the upper bound if guess was too high
    elif feedback == 'l':
        low = guess + 1   # Adjust the lower bound if guess was too low
    # No action needed if feedback == 'c', loop will terminate

print(f"I've guessed it! Your number was {guess}.")
