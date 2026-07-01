"""
Question: 2: Count the frequency of each word in a sentence using a dictionary.

"""

sentence = "Apple banana apple orange banana apple"

words = sentence.lower().split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)