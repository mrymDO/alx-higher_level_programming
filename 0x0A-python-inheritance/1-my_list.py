#!ust/bin/python3
"""Module 1-my_list a class that inherit from another"""

class MyList(list):
    """Subclass of list"""

    def print_sorted(self):
        print(sorted(self))
