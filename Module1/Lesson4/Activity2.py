amount = int(input("Enter the amount: "))

note_100 = amount//100
note_50 = (amount%100)//50
note_10 = ((amount%100)%50)//10

print("Notes of 100tk", note_100)
print("Notes of 50tk", note_50)
print("Notes of 10tk", note_10)