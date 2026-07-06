"""
Question: 4: Write a program that saves a list of dictionaries (student records) to a JSON file, then loads them back.

"""

import json

user_data = [
    {"id": 1, "name": "Ahmad", "role": "Admin"},
    {"id": 2, "name": "Zainab", "role": "User"},
    {"id": 3, "name": "Ali", "role": "Guest"}
]

with open("user.json", "w") as file:
    print("Saving Data in the file...")
    json.dump(user_data, file, indent=4)

print("User Data succesfully save in file user.json")

with open("user.json", "r") as file:
    content = file.read()
    print(content)

