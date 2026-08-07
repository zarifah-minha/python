try:
    number = int(input("Please enter a number:"))
    print("The number you entered", number)
except ValueError:
    print("This is invalid. Please enter a valid number.")