import math

buying_price = int(input("Enter the buying price: "))
selling_price = int(input("Enter the selling price: "))

amount = math.fabs(selling_price - buying_price)

if buying_price > selling_price :
    print(f"You have {amount}tk loss")
else:
    print(f"You have {amount}tk profit")