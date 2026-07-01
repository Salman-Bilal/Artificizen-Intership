"""
Question: 3: Find duplicate elements in a list using a set.

"""

numbers = [1, 2, 3, 4, 5, 2, 6, 3, 7, 5]

unique_num = set()
duplicate_num = set()

for num in numbers:
    if num in unique_num:
        duplicate_num.add(num)
    else:
        unique_num.add(num)


print(duplicate_num)
