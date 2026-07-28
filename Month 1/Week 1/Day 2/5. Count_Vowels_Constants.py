"""
Question: 5: Given a sentence, count the vowels and consonants separately.

"""

sentence = "Aritificizen"

vowels = "aeiou"

vowels_count = 0
consonants_counts = 0

for char in sentence.lower():
    if char.isalpha():
        if char in vowels:
            vowels_count += 1
        else:
            consonants_counts += 1

print(f"Total Vowels Count: {vowels_count}")
print("Total Consonants Counts: {} ".format(consonants_counts))            
