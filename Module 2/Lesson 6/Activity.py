guess = int(input("Enter a number: "))
secret = 27
attempts = 0

while attempts < 5:
    attempts= attempts+1
    if guess == secret:
        print("YOU WIN!")
        break
    elif guess > secret:
        print("HINT: Your number is too high")
    else:
        print("HINT: Your number is too low")

    print("Lives left: ", end="")

    for i in range(5):
        print("heart", end=" ")

    print()

if guess != secret:
    print("You lost")
    print("The number was: ", secret)