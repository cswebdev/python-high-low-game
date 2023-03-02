# import random


# def play():
#     random_number = random.randint(1, 10)
#     counter = 0
#     while counter < 3:
#         counter += 1
#         guess = int(input("Guess a number between 1 and 10: "))

#         if guess - - random_number:
#             print("Congratulations! You guessed the number")
#             break
#         elif guess < random_number:
#             print('Your guess was too low.')
#         else:
#             print('Your guess was too high.')

#         if counter == 3:
#             print('Sorry. you ran out of guesses. Try again!')
#     if __name__ == '__main__':
#         play()


import random


computer = random.randint(1, 10)

guesses = 0
print("You have 3 attempts to guess the right number")
while guesses <= 2:
    guess = int(input(""))
    guesses += 1
    if guess != computer:
        print("try again")
        print(guesses)
    else:
        print("you win, you guessed ", guess,
              "and the correct number was ", computer)
    if guesses >= 2:
        print("You ran out of attempts, you lose!")
        break


# print(computer)
