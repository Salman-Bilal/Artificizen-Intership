"""
Question: 6: Write a function with a default argument, and add a comment explaining why mutable default arguments (like a list) are risky in Python.

"""
def append_to_list(element, current_list=None):
   """ 
    WHY WE USE 'None' INSTEAD OF '[]' HERE:
    Think of Python as a bit lazy when it reads this function definition. 
    If we put 'current_list=[]' up there, Python creates exactly ONE shared 
    box (list) in its memory and reuses that same box every single time 
    the function is called.
    
    So, if you added "Apple" on the first call, and "Banana" on the second call,
    the second call would accidentally include the "Apple" from before! It's 
    like a shared shopping cart that never gets emptied.
    
    By using 'None', we tell Python: "Hey, if the user didn't bring their own 
    list, give them a brand-new, completely empty cart just for this trip."
    
    """
   if current_list is None:
        current_list = []  
   current_list.append(element)
   return current_list

cart1 = append_to_list('apple')
print(cart1)

cart2 =append_to_list('banana')
print(cart2)