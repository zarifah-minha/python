# List Comprehension
items = ["eraser","notebook","pencil","sharpener","glue"]
stock_count = [0,12,8,5,3]

in_stock = [item for item in items if item != "eraser"]
print("In stock item: ", in_stock)

#Dictionary comprenhesion
inventory = {
    item : count for item, count in zip(items,stock_count)
}
print("Inventory:",inventory)

chosen_item = input("Which item do you want to buy?").lower()

if chosen_item not in inventory:
    print(f"(chosen_item) is stock out.")
    exit()

prices = [5,10,40,15,20]
markup = int(input("Enter the markup price that you want to add every price!"))

markedup_prices = list(map(lambda p : p + markup, prices))
print("Marked up prices: ", markedup_prices)

item_index = items.index (chosen_item)
chosen_price = markedup_prices[item_index]
print(f"Marked up prices of {chosen_item} : : {chosen_price}")

inventory[chosen_item] = inventory[chosen_item] - 1
print(f"{chosen_item} purchased. Remaining stock: {inventory[chosen_item]}")