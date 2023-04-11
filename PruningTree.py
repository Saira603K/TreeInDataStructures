'''mplement a pruning function/method which takes in a binary tree t and a depth k, and
should return a new tree that is a copy of only the first k levels of t. '''

import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def prune_tree(root, k):
    if root is None or k == 0:
        return None

    pruned_root = copy.deepcopy(root)
    prune_helper(pruned_root, 1, k)
    return pruned_root

def prune_helper(node, current_level, max_level):
    if node is None:
        return

    if current_level == max_level:
        node.left = None
        node.right = None
        return

    prune_helper(node.left, current_level + 1, max_level)
    prune_helper(node.right, current_level + 1, max_level)

def print_level_order(root):
    if root is None:
        return

    queue = [root]

    while queue:
        level_count = len(queue)

        while level_count > 0:
            node = queue.pop(0)

            print(node.value, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            level_count -= 1

        print()


# Example usage:
root = Node(5)
root.left = Node(4)
root.right = Node(3)
root.left.left = Node(3)
root.left.right = Node(2)
root.right.left = Node(2)
root.right.right = Node(1)
root.left.left.left = Node(2)
root.left.left.right = Node(1)
root.left.right.left = Node(1)
root.right.left.left = Node(0)
root.left.left.left.left = Node(1)

print("Original tree:")
print_level_order(root)

k = 3
pruned_root = prune_tree(root, k)

print("\n\nPruned tree with depth {}:".format(k))
print_level_order(pruned_root)


'''output:
Original tree:
5 
4 3 
3 2 2 1 
2 1 1 0 
1 


Pruned tree with depth 3:
5 
4 3 
3 2 2 1 
'''
