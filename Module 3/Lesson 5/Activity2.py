import random

while True:
    user_action = input("Enter a choice (rock/paper/scissors):")
    possible_action = ["rock","paper","scissors"]
    computer_action = random.choice(possible_action)
    print(f"You chose {user_action} and compter chose {computer_action}")

    if user_action == computer_action:
        print("It is a Tie!")
    elif user_action == "rock":
        if computer_action == "paper":
            print("Paper covers rock. You lose!")
        else:
            print("Rock smashes scissors. You win!")

    elif user_action == "rock":
           if computer_action == "paper":
               print("Paper covers rock. You lose!")
           else:
               print("Rock smashes scissors. You win!")
               
    elif user_action == "scissors":
               if computer_action == "rock":
                   print("Paper smashes scissors. You lose!")
               else:
                   print("scissors cut paper. You win!")

    playAgain = input("Play again (yes/no)?")
    if playAgain == "no":
         break
                