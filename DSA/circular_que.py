class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.items = [None]*size #makes a list of size (N) which has default value as None
        self.front = self.rear = -1

    # Insertion of element
    def enqueue(self,value):
        if ((self.rear + 1)  == self.front):
            print("Queue is full")
        
        # empty queue
        elif self.front == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value
        
        else:
            self.rear = (self.rear + 1)% self.size
            self.items[self.rear] = value
        
    # Deletion of element
    def dequeue(self):
        if(self.front == -1):
            print("Queue is empty")
        elif self.front == self.rear:
            print(self.items[self.front])
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            self.front = (self.front + 1)% self.size


cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(10)
cq.enqueue(10)
cq.enqueue(10)