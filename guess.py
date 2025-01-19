import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Ask the user to guess the number
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Run the game
guess_the_number()
