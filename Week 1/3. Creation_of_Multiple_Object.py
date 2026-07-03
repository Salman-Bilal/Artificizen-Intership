"""
Question: 3: Demonstrate the difference between instance and class variables: track how many objects of a class have been created.

"""
class ObjectTracker:
    # Class Variable
    counter = 0

    def __init__(self, item_name):
        # Instance Variable
        self.item_name = item_name

        # Increment the class variable
        ObjectTracker.counter += 1



instance_one = ObjectTracker("Laptop")

print("Objects Created:", ObjectTracker.counter)


instance_two = ObjectTracker("Phone")

print("Objects Created:", ObjectTracker.counter)