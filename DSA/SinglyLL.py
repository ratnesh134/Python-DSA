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

    def insertAtBeg(self,value):
        temp = Node(value) # Creates a node
        temp.next = self.head
        self.head = temp

    def insertionAtMid(self,value,x): # x is the value after which "value" will be added
        temp = Node(value)
        t1 = self.head

        while (t1.next != None):
            if (t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    # Deleting the linked list
    def deleteLinkedList(self,value):

        t1 = self.head
        prev = self.head

        # If element we want to delete is at the start
        if(self.head == value):
            self.head = t1.next

        # If element we want to delete is in the middle
        while (t1.next != None):

            if(t1.data == value):
                prev.next = t1.next
                break

            else:
                prev = t1
                t1 = t1.next

        # If we want to delete element at the end
        if (t1.data == value):
            prev.next = None


    
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
obj.insertAtBeg(50)
obj.insertionAtMid(60,20)
obj.deleteLinkedList(60)
obj.printLL()
