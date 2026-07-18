def greet_customer():
    print("Welcome Lemonade stand! \n Fresh lemonade just for you")

greet_customer()

price_per_cup = float(input("Enter the price of the cups: "))
cups_sold = int(input("Enter the total cups sold: "))

def calculate_total (price_per_cup, cups_sold):
    total = price_per_cup * cups_sold
    return total

total_cost = calculate_total(price_per_cup, cups_sold)
print("total cost: ", total_cost)

amount_paid = float(input("Enter the amount paid by the customer: "))

def calculate_change (amount_paid, total_cost):
    change = amount_paid - total_cost
    return change

print("Change: ", calculate_change(amount_paid,total_cost))

def thankyou_msg (cups_sold):
    if cups_sold >= 5 :
        return "WOW! Big order.Thank you for so much support"
    
    else:
        return "Thank you for stopping by!"
    
print(thankyou_msg(cups_sold))