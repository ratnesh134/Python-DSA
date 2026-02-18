class Node:

    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class SinglyLL:

    def __init__(self,head=None):
        self.head = head

    # Insert at end
    def insertAtEnd(self,value):
        temp = Node(30)
        if (self.head != None):
            t1 = self.head
        
            while (t1.next != None):
                t1 = t1.next
            t1.next = temp
        
        else:
            self.head = temp
        

