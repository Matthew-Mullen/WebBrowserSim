#----------------------------------------------------
# Stack implementation #2 
# (Top of stack corresponds to back of list)
# 
# Author: CMPUT 175 team
# Updated by:
#----------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def pop(self):
        if self.isEmpty()==True:
            raise Exception('Stack is empty cannot pop')
        if self.isEmpty()==False:

            return self.items.pop()
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def peek(self):
        if self.isEmpty()==True:
            raise Exception('Stack is empty cannot pop')
        if self.isEmpty()==False:
            
            
            return self.items[len(self.items)-1] 
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
    
    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
           for i in range(len(self.items)):
                self.items.pop()
                