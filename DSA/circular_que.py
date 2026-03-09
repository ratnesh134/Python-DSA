class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.items = [None]*size #makes a list of size (N) which has default value as None
        self.front = self.rear = -1

    # Insertion of element
    def enqueue(self,value):
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is full")
        
        # empty queue
        elif self.front == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value
        
        else:
            self.rear = (self.rear + 1)% self.size
            self.items[self.rear] = value
        
    
