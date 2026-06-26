print("select your ride : ")
print("1.Bike")
print("2.Car")

choice = int(input("Enter your choice (1/2): "))

if choice == 1:
    print("What type of bike do you want?")
    print("1.Yamaha Bike")
    print("2. Electric Bike")

    choice2 = int(input("Enter your choice (1/2): "))
    if choice == 1:
        print("You have selected Yamaha Bike")
    else:
        print("You have selected Electric Bike")

elif choice == 2:
    print("What type of car do you want?")
    print("1.F Premio")
    print("2.Toyota Hiace ")

    choice2 = int(input("Enter your choice (1/2): "))
    if choice == 1:
        print("You have selected F Premio Bike")
    else:
        print("You have selected Toyota Hiace")

else:
    print("Invalid Choice!")