"""
Question: 1: Write a function that accepts any number of arguments and returns their sum (use *args).

"""
def Addition(*arg):
    return sum(arg)

print(Addition(1,2,3,4))
