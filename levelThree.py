from statistics import median
import random

playerinput = int(input("Enter a number:"))

low = 1
high = 10
attempt = 0

guess = (low+high)//2

while guess != playerinput:
    guess = (low+high)//2
    # print("Computer guesses:", guess)
    if guess > playerinput:
        high = guess
        print("your guess:", guess, "is too low")
        attempt += 1
    if guess < playerinput:
        low = guess + 1
        print("your guess:", guess, "is too high")
        attempt += 1
    elif guess == playerinput:
        print("congrats", guess,
              "is the right number. It took you", attempt+1, "tries")


