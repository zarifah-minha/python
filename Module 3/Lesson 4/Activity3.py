valid = False
while not valid:
    try:
        num = int(input("Please enter a number: "))
        while num%2 == 0:
            print ("BYE")
            valid = True
    except ValueError:
        print("Invalid")