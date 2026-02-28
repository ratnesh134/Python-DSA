class Queue:

    def __init__(self):
        self.items = []

    
    def isEmpty(self):
        return len(self.items) == 0
    
    def insertElement(self,value):
        return self.items.append(value)
    
    def popElement(self):
        return self.items.pop(0)
    
    