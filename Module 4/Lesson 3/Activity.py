my_dictionary = {
    "name" : "Sarah",
    "age" : 13,
    "school" : "sunshine school",
    "grade" : 8
}
print(my_dictionary)

# Length
print("Length", len(my_dictionary))

#Accessing items with key
print(my_dictionary["name"]) #Approach 1
print(my_dictionary.get("name")) #Approach 2

# Adding and updating value
my_dictionary["country"] = "Bangladesh"
print(my_dictionary)
my_dictionary["school"] = "Mastermind school"
print(my_dictionary)

#Iterating using a loop
for item in my_dictionary:
    print(my_dictionary[item])

#Deleting one item
my_dictionary.pop("country")
print(my_dictionary)

#clear everything
my_dictionary.clear()
print(my_dictionary)