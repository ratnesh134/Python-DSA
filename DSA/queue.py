class Queue:

    def __init__(self):
        self.items = []

    
    def isEmpty(self):
        return len(self.items) == 0
    
    def insertElement(self,value):
        return self.items.append(value)
    
    def popElement(self):

        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.items.pop(0)


q = Queue()
q.insertElement(10)
q.insertElement(20) 
q.insertElement(30)
q.insertElement(40)  
print(q.popElement())
print(q.popElement())
print(q.popElement())
print(q.popElement())
