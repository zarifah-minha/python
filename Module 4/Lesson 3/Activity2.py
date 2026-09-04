my_dictionary = {
    "codingal" : 2,
    "is" : 2,
    "best" : 2,
    "for" : 2,
    "coding" : 1
}
print("Original dictionary:",my_dictionary)

k = 2
count = 0

for item in my_dictionary:
    if my_dictionary[item] == k:
        count += 1

print(f"Frequency of {k}: {count}")