import random

def game():
        
    C_number = random.randrange(1,101)
    userInput = int(input("Enter your number: "))

    if userInput > C_number:
        print("Computer number: ",C_number)
        print("your guess number is too high")
    elif C_number > userInput:
        print("Computer number: ",C_number)
        print("your guess number is too low")
    else:
        print("Computer number: ",C_number)
        print("your guess number is equal")

    game() # recursion
game()