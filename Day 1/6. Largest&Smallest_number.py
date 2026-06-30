"""
Question: 6: Given a list of numbers, find the largest and smallest without using min()/max().

"""
num_list = [42, 32, 52, 22, 45, 16, 28, 70]

largest_num = smallest_num = num_list[0]

for num in num_list:
    if num < smallest_num:
        smallest_num = num
    if num > largest_num:
        largest_num = num

print(f"{largest_num} is the largest number")
print(f"{smallest_num} is the smallest number")