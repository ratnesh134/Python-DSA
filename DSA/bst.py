# Binary Search Tree

class Node:

    def __init__(self,value):

        self.left = None
        self.right = None
        self.data = value

    # Insertion of Node
    def insert(root,value):  # Here current Node is pointed to root

        if (root == None):
            return Node(value)
        
        if (root.data == value):
            return root
        
        if (root.data > value):
            root.left =  insert(root.left,value)
        else:
           
            root.right =  insert(root.right,value)
        
        return root

def inOrder(root):
    if (root != None):
        
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)


