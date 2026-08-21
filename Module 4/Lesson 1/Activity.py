my_list = ["codingal", 2012, 34.55, True]
print(my_list)

# Length of the list
print(len(my_list))

# Accesing a particular item from the list
print(my_list[2])
print(my_list[0]) #FIRST item
print(my_list[-1]) #LAST item

# Slicing
print(my_list[1:4]) # my_list[start_index:end-index+1]

# iterating through a loop
for item in my_list:
    print(item)

# Use * operator
print(my_list * 3)

# Reversing a list
print(my_list[::-1])