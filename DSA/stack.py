class Stack:
    
    def __init__(self):
        self.ls = []
    
    # to find the lenth of the stack
    def stack_length(self):

        return len(self.ls)
    
    # to insert element into stack
    def push(self,value):
        self.ls.insert(0,value)



    
