"""A number guessing game!"""

import random

secret: int = random.randint(1, 10)
print("I am thinking of a number between 1 and 10...")

guess: int = -1
guesses: int = 0
while guess != secret:
    guesses += 1
    guess = int(input("What's your guess? "))
    if guess == secret:
        print(f"Wow, you guessed it in {guesses} tries! Good job! :)")
        break
    elif guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("Congratulations!")
