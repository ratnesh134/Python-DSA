class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.items = [None]*size #makes a list of size (N) which has default value as None
        self.front = self.rear = -1

    