# Node Creation
class Node  :

    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
    
# Pre Order Traversal Logic
def preorder(root):
    if (root != None):
        print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)



root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)

