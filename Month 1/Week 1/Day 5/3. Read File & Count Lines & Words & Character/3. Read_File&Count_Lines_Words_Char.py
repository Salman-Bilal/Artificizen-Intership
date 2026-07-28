"""
Question: 3: Write a program that reads a text file and reports the number of lines, words, and characters.

"""

try:
    with open("test_file.txt", "r", encoding="utf-8") as file:
        
        content = file.read()
        
        char_count = len(content)

        list_of_word = content.split()
        total_words = len(list_of_word)

        list_of_lines = content.splitlines()
        total_lines = len(list_of_lines)

        print(f"Total Lines in this file:      {total_lines:,}")
        print(f"Total Words in this file:      {total_words:,}")
        print(f"total Characters in this file: {char_count:,}\n")

except FileNotFoundError:
    print(" Error: The file  could not be found.")