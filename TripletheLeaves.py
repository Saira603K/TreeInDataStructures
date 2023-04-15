'''TRIPLE ALL THE LEAVES IN THE BINARY TREE'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def triple_leaves(node):
    if node is None:
        return

    if node.left is None and node.right is None:
        node.value *= 3
    else:
        triple_leaves(node.left)
        triple_leaves(node.right)

def print_level_order(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        print(node.value, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage:
# Example usage:
# Creating a simple binary tree
#       4
#      / \
#     2   6
#    / \ / \
#   1  3 5  7
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print("Before tripling the leaves:")
print_level_order(root)

triple_leaves(root)
# Now the tree should look like this:
#       4
#      / \
#     2   6
#    / \ / \
#   3  9 15 21

print("\nAfter tripling the leaves:")
print_level_order(root)
