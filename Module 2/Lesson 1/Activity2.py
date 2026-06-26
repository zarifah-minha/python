units = int(input("Enter the number of units consumed: "))

if units < 50:
    total = 2.60*units + 25
elif units <= 100:
    total = 3.25*units + 35
elif units <= 200:
    total = 5.26*units + 45
elif units > 200:
    total = 8.45*units + 75
else:
    print("Invalid Input")

print(f"Your electricity bill is {total}")