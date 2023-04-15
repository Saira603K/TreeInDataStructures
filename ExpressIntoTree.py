'''The arithmetic expression can be converted to a binary tree structure, where all leaves
are numbers and all inner-node labels are operators (just considering 7 operations: +, -, *,
/, //, %, **), such as the following binary tree for the expression: 3 + ((5+9)*2). Define a
function/method eval(t) to calculate the expression value denoted by t'''


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def eval(t):
    if t is None:
        return 0

    # If it's a leaf node, return its value
    if t.left is None and t.right is None:
        return t.value

    # Calculate the values of the left and right subtrees
    left_val = eval(t.left)
    right_val = eval(t.right)

    # Perform the operation corresponding to the node's value
    if t.value == '+':
        return left_val + right_val
    elif t.value == '-':
        return left_val - right_val
    elif t.value == '*':
        return left_val * right_val
    elif t.value == '/':
        return left_val / right_val
    elif t.value == '//':
        return left_val // right_val
    elif t.value == '%':
        return left_val % right_val
    elif t.value == '**':
        return left_val ** right_val

root = TreeNode('+')
root.left = TreeNode(3)
root.right = TreeNode('*')
root.right.left = TreeNode('+')
root.right.left.left = TreeNode(5)
root.right.left.right = TreeNode(9)
root.right.right = TreeNode(2)

result = eval(root)
print("Result:", result)

# Example usage:
# Expression: 3 + ((5 + 9) * 2)
# Tree structure:
#       +
#      / \
#     3   *
#        / \
#       +   2
#      / \
#     5   9

#OUTPUT:
#Result: 31
