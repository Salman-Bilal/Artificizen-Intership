"""
Question: 4: Merge two dictionaries; if a key exists in both, sum the values.
"""

dict_1 = {"a": 1, "b": 2, "c": 5}
dict_2 = {"e": 2, "b": 2, "f": 6}

merge_dict = dict_1.copy()

for key, value in dict_2.items():
    if key in merge_dict:
        merge_dict[key] += value
    else:
        merge_dict[key] = value


print(merge_dict)

