"""
Question: 5:  Check if a given string is a palindrome

"""
text = input("Enter a String: ")
i = 0
j = len(text) - 1

palindrome = False
while i < j:
    if text[i] == text[j]:
        palindrome = True
    else:
        palindrome = False
    i = i + 1
    j = j - 1

if palindrome:
    print(f"{text} is a palindrome string")

