student_data = {
    "id1": {"name": "Anha", "class": "VIII", "subject": "English, Math, Science"},
    "id2": {"name": "Tahmid", "class": "VIII", "subject": "ICT, Math, BGS"},
    "id3": {"name": "Medha", "class": "VIII", "subject": "Biology, English, Chemistry"},
    "id4": {"name": "Ayman", "class": "VIII", "subject": "Physics, ICT, Math"}
}
 
print("Original Student Records:")
print(student_data)

print("")
print("Details of id1:")
print(student_data.get("id1", "Not Found"))
 
print("")
print("Details of id5:")
print(student_data.get("id5", "Not Found"))

student_data["id5"] = {
    "name": "Minha",
    "class": "VIII",
    "subject": "Biology, English, Geography"
}
 
print("")
print("After adding id5:")
print(student_data)

student_data["id2"]["subject"] = "English, Math, Biology"
 
print("")
print("After updating id2 subject:")
print(student_data["id2"])

cleaned_data = {}
seen_records = []
 
for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject"])
 
    if unique_key not in seen_records:
        seen_records.append(unique_key)
        cleaned_data[student_id] = details
 
student_data = cleaned_data
 
print("")
print("After removing duplicate records:")
print(student_data)

removed_student = student_data.pop("id4", "Student not found")
 
print("")
print("Removed student:")
print(removed_student)
print("")
print("Total student records left:", len(student_data))
print("")
print("Final Student Subject Records")
 
for student_id, details in student_data.items():
    print(student_id, ":", details)