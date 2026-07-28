"""
Question: 6: Write a function that returns the most frequent element in a list.
"""

def ferquent_num(nums):
    if not nums:
        return None
    return max(nums, key=nums.count)

numbers = [1, 2, 3, 1, 4, 2, 2, 1, 4, 1]

print(f"Most Frequent Number: {ferquent_num(numbers)}")