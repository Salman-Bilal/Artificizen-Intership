"""
Question: 2: Reverse a string without using slicing or a built-in reverse function.

"""
string = 'artificizen'

reverse_string = ""

for char in string:
    reverse_string = char + reverse_string

print(reverse_string)    
