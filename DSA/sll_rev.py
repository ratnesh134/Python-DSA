class Node:

    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class SinglyLL:

    def __init__(self,head=None):
        self.head = head

    # Insert at end
    def insertAtEnd(self,value):
        temp = Node(value)
        if (self.head != None):
            t1 = self.head
        
            while (t1.next != None):
                t1 = t1.next
            t1.next = temp
        
        else:
            self.head = temp
        

    def insertAtBegin(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp


    def insertAtMid(self,value,x):
        # x contains that node value after which we need to insert
        temp = Node(value) # Node creation
        t1 = self.head

        while (t1.next != None):
            if (t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def deleteLL(self,value):
        t1 = self.head
        prev = t1
        while (t1.next != None):
            if (t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        

    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)




obj = SinglyLL()
obj.insertAtEnd(40)
obj.insertAtEnd(20)
obj.insertAtEnd(60)
obj.insertAtBegin(70)
obj.insertAtMid(90,20)
obj.deleteLL(20)
obj.printLL()
