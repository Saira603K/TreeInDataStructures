'''Define a function or write a method Fib_tree(n) in a class to create Fibonacci tree based
on Fibonacci sequence, such as 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... ..., and n (starting
from 1) is 𝑛𝑡ℎ term in the series.'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def Fib_tree(n):
    if n <= 0:
        return None

    node = Node(fibonacci(n-1))
    node.left = Fib_tree(n - 1)
    node.right = Fib_tree(n - 2)

    return node

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
root1 = Fib_tree(7)
print("Fib_tree(7):")
print_level_order(root1)

print("\n")

'''output:
Fib_tree(7):
8 5 3 3 2 2 1 2 1 1 1 1 1 1 0 1 1 1 0 1 0 0 1 0 0 0 1 0 0 0 0 0 0 
'''
#Example :
'''
root1 = Fib_tree(6)
print("Fib_tree(6):")
print_level_order(root1)

output:
Fib_tree(6):
5 3 2 2 1 1 1 1 1 1 0 1 0 0 1 0 0 0 0 0 
'''
