import random

playing = True
number = str(random.randint(0,9))

print("I will generate a number between 0 to 9. You have to guess the number one at a time.")

while playing:
    guess = input("Enter your guess: ")
    if  number == guess:
        print("You win the game!")
        print("The number was: ", number)
        break
    else:
        print("Wrong Answer!! Try Again.")