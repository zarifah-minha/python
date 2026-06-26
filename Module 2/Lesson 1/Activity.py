medical_cause = input("Do you have any medical conditions? (y/n)").lower()

if medical_cause == "y":
    print("Allowed")
else:
    attendance = int(input("Enter your attendance: "))
    if attendance > 75:
     print("Allowed")
    else:
     print("Not allowed")