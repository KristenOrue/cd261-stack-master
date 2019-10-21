# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# YOUR NAME

class Stack:

    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
 


 
