import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

guess = 0
guesses = 0

while guess != number:
    guess = int(input("Guess the number between 1 and 100: "))
    guesses += 1

    if guess > number:
        print("Lower number please!")

    elif guess < number:
        print("Higher number please!")

    else:
        print("Congratulations! You guessed the number.")
        print(f"You guessed it in {guesses} guesses.")