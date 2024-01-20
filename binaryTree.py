# Checking if a binary tree is a complete binary tree in C

class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

if __name__ == '__main__':
    # create root
    root = Node(1)
    ''' following is the tree after above statement
    1
    / \
    None None'''

    root.left = Node(2)
    root.right = Node(3)
    ''' 2 and 3 become left and right children of 1
       1
      /  \
     2    3
    / \  / \
    None None None None'''
    root.left.left = Node(4)





