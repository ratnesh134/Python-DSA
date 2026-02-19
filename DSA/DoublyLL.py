class Node:
    def __init__(self,info,prev=None,next=None):
        self.data = info
        self.next = next
        self.prev = prev


class DoublyLL:

    def __init__(self,head = None):
        self.head = head

    # Insertion at the end
    def insertionAtEnd(self,value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        
        else:
            t = self.head
            while(t.next != None):
                t = t.next

            t.next = temp
            temp.prev = t


    def printDLL(self):
        t = self.head
        while (t.next != None):
            print(t.data)
            t = t.next
        print(t.data)


obj = DoublyLL()
obj.insertionAtEnd(30)
obj.insertionAtEnd(40)
obj.insertionAtEnd(50)
obj.insertionAtEnd(60)
obj.printDLL()


    