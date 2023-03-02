import random 

user_number = int(input('Pick a number between 1 and 10.'))
counter = 0

while counter < 3: 
    counter +=1
    computer_number = random.randint(1,10)
    print('The computer guessed', computer_number)
    break
if counter == 3: 
    print('You win. The computer did not guess your number')

# import random


# guesses = 0
# guess = int(input("Enter a number: "))
# while guesses <= 2:
#     computer = random.randint(1, 10)
#     guesses += 1
#     if computer != guess:
#         print("try again", computer, " is not correct")
#     else:
#         print("computer wins, it guessed ", computer,
#               "and the correct number was ", guess)
#         break