# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# KRISTEN ORUE

class Stack:

    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError()
        else:
            return self.items[len(self.items)-1]

    def push(self, item):
        self.items.append(item)
 


 
