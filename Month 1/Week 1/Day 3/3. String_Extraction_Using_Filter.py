"""
Question: 3: Use filter() to extract all strings longer than 5 characters from a list.

"""

string_list =  [ "Wolves", "are", "hunting", "animals", "People","are", "playing", "winter", "sports" ]

string = list(filter(lambda s: len(s) > 5, string_list))

print(string)