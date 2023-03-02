

print("Play guessing game! Who wants to make a number to guess? You or the computer?")
print("Enter y to play against the computer")
print("Enter n to have the computer play against you")

input = input("")

if input == "y":
    print("Guess a number between 1-10")
    import levelOne
if input == "n":
    print("The computer is going to guess between 1-10")
    import levelThree
