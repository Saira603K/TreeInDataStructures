# Python3 program to convert a Binary Tree to Threaded Tree
 
# A utility function to create a new node
class newNode:
    def __init__(self, key):
        self.left = self.right = None
        self.key = key
        self.isThreaded = None
         
# Converts tree with given root to threaded binary tree. This function returns rightmost child of root.
def createThreaded(root):
     
    # Base cases : Tree is empty or has single node
    if root == None:
        return None
    if root.left == None and root.right == None:
        return root
 
    # Find predecessor if it exists
    if root.left != None:
         
        # Find predecessor of root (Rightmost child in left subtree)
        l = createThreaded(root.left)
 
        # Link a thread from predecessor
        # to root.
        l.right = root
        l.isThreaded = True
 
    # If current node is rightmost child
    if root.right == None:
        return root
 
    # Recur for right subtree.
    return createThreaded(root.right)
 
# A utility function to find leftmost node in a binary tree rooted with 'root.This function is used in inOrder()
def leftMost(root):
    while root != None and root.left != None:
        root = root.left
    return root
 
# Function to do inorder traversal of a threaded binary tree
def inOrder(root):
    if root == None:
        return
 
    # Find the leftmost node in Binary Tree
    cur = leftMost(root)
 
    while cur != None:
        print(cur.key, end = " ")
 
        # If this Node is a thread Node, then
        # go to inorder successor
        if cur.isThreaded:
            cur = cur.right
 
        else: # Else go to the leftmost child
              # in right subtree
            cur = leftMost(cur.right)
 
# Driver Code
#       1
#      / \
#     2   3
#    /   / \
#   4   5   6 
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.right.left = newNode(5)
root.right.right = newNode(6)

createThreaded(root)

print("Inorder traversal of created", "threaded tree is")
inOrder(root)
