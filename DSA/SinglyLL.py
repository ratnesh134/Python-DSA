class Node:

    # Constructor
    def __init__(self,info,next=None):
        self.data = info
        self.next = next


class SinglyLinkedList:

    # Constructor
    def __init__(self,head=None):
        self.head = head
    
    def insertAtEnd(self,value):
        temp = Node(value)

        # When Linked List is already created
        if (self.head != None):
            t1 = self.head

            while (t1.next != None):
                t1 = t1.next
            t1.next = temp

        # When the Linked List is not created
        else:
            self.head = temp
        
    
    # Printing the Linked List

    def printLL(self):

        t1 = self.head
        while (t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj = SinglyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.printLL()
