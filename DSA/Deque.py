class Deque:

    def __init__(self):
        self.items = []

    
    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtEnd(self,value):
        return self.items.append(value)
    
    def deleteAtFront(self):

        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.items.pop(0)
    
    def insertAtBeg(self,value):
        self.items.insert(0,value)
        