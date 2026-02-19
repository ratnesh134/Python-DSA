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

    # Insertion at Beginning
    def insertionAtBeg(self,value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    # Insertion in the middle
    def insertionAtMid(self,value,x):
        # x is the value/data after which we insert the node
        temp = Node(value)
        t = self.head

        # Element Search
        while(t.next != None):
            if (t.data == x):
                break

            else:
                t = t.next
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t


    # Deletion of Node
    def deletionOfNode(self,value):
        t = self.head
        if self.head == None:
            print("Linked List is empty")
            return
        else:
            t = self.head
            # deletion at the beginning
            if (self.head.data == value):
                self.head = t.next
                self.head.prev = None
                return
            
            # deletion at the middle
            while(t.next != None):
                if (t.data == value):
                    t.prev.next = t.next
                    t.next.prev = t.prev
                    return
                else:
                    t = t.next
            # deletion at the end
            if (t.data == value):
                t.prev.next = None




    def printDLL(self):
        t = self.head
        while (t.next != None):
            print(t.data,end=" <--> ")
            t = t.next
        print(t.data)


obj = DoublyLL()
obj.insertionAtEnd(30)
obj.insertionAtEnd(40)
obj.insertionAtEnd(50)
obj.insertionAtEnd(60)
obj.insertionAtBeg(5)
obj.insertionAtMid(100,50)
obj.deletionOfNode(40)
obj.printDLL()


    