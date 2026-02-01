# Random guessing Game
import random


input("Welcome to the Guessing Game! Press Enter to start...\n")
top_range = input("Enter the upper limit for the guessing range: ")

if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range < 0:
        print("Please enter a number greater than 0 next time.")
        quit()
else:
    print("Please enter a valid number next time.")
    quit()


num = random.randint(1,top_range)
tries = 0

while True:
    guess = (input(f"Guess a number between 1 and {top_range}: "))
    if guess.isdigit():
        guess = int(guess)
        if guess < 1 or guess > top_range:
            print(f"Please guess a number within the range of 1 to {top_range}.")
            continue
    else:
        print("Please enter a valid number.")
        continue
    
    if num == guess:
        tries += 1
        print(f"Congratulations! You guessed the correct number in {tries} tries.")
        break
    elif num < guess:
        tries += 1
        print("Too high! Try again.")
    elif num > guess:
        tries += 1
        print("Too low! Try again.")
    else:
        print("Invalid input. Please enter a valid number.")