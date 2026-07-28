"""
Question: 5: Sort a list of dictionaries (e.g., students with name and marks) by marks using sorted() and a key function.

"""
import json 

student_data = [
    {"name": "Ali", "marks": 82},
    {"name": "Ahmad", "marks": 74},
    {"name": "Hamza", "marks": 69},
    {"name": "Momin", "marks": 66},
    {"name": "Bilal", "marks": 79},
    {"name": "Saad", "marks": 64},
    {"name": "Ammar", "marks": 89}
]

sorted_data = sorted(student_data, key=lambda stud: stud["marks"], reverse=True)

print(json.dumps(sorted_data, indent=4))