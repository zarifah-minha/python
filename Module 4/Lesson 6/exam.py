students = {"Alice": 85, "David": 72, "Charles": 91, "Emma": 64, "Bob": 78}

# Class Average
total = 0

for score in students.values():
    total += score

average = total / len(students)
print("Class average:", average)

# Find highest and lowest scores
highest = max(students.values())
lowest = min(students.values())

top_student = max(students,key=students.get)
bottom_student = min(students,key=students.get)
print("Lowest score:",lowest,"-",bottom_student)
print("Highest score:", highest,"-", top_student)

# Look up a student's grade
name = input("Enter a student's name: ")
score = students.get(name)

if score is not None:
    print(name, "scored", score)
else:
    print("Sorry, that studnet is not in the grade book")