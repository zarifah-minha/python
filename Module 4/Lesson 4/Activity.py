set1 = {"Apple", "Kiwi", "Kiwi", "Mango,", "Banana", "Watermelon", "Mango", "Guava"}
print(set1)

#Adding an item 
set1.add("Pineapple")
print(set1)

set2 = {"Jackfruit", "Peach", "Apple", "Strawberry", "Kiwi"}
#Set Intersection -> common items between two sets
print("Set Intersection:",set1.intersection(set2))

import array as arr
fruits_count = arr.array("i", [3,5,4,2])
print(fruits_count)

# Adding a new fruit count
fruits_count.insert(0,1)
print(fruits_count)
fruits_count.append(4)
print(fruits_count)

#count of any item
print("Number of times 4 repeated:", fruits_count.count(4))

# Reverse
fruits_count.reverse()
print("Reversed array:", fruits_count)