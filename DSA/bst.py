# Binary Search Tree

# Creation of Nodes
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


# Searching of Node
def search(root,value):  # Here current Node is pointed to root

    if (root == None):
        print("Element Not found")
    
    if (root.data == value):
        print("Element found")
    
    if (root.data > value):
        search(root.left,value)
    else:
        
        search(root.right,value)
    



def inOrder(root):
    if (root != None):
        
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)

root = insert(None,20)
root = insert(root,15)
root = insert(root,30)
root = insert(root,40)
root = insert(root,12)
root = insert(root,18)
root = insert(root,50)

inOrder(root)