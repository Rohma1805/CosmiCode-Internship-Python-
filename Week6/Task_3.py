#Task3:
import json
#Sample data
student_data = {
    "name": "Rohma",
    "age": 21,
    "courses": ["Python", "AI", "ML"]}
#1.Write data to JSON file
with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4)
print(" Data written to student.json")
#2.Read data back from JSON file
with open("student.json", "r") as file:
    loaded_data = json.load(file)
print("\n Data read from JSON file:")
print(loaded_data)
#3.Access specific values
print("\nStudent Name:", loaded_data["name"])
print("Enrolled Courses:", loaded_data["courses"])
