class Stack:
    
    def __init__(self):
        self.ls = []
    
    # to find the lenth of the stack
    def stack_length(self):

        return len(self.ls)
    
    # to insert element into stack
    def push(self,value):
        self.ls.insert(0,value)

    # to see the latest element 
    def peek(self):
        if len(self.ls) == 0:
            raise Exception("Empty Stack/List")
        else:
            return self.ls[0]
    
    # delete element
    def pop(self):
        if len(self.ls) == 0:
            raise Exception("Empty Stack/List")
        else:
            return self.ls.pop(0) # Need to specify the index since we are using the insert function instead of append
        

    
        
        
    
    




    
