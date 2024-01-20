class Node:
    # Constructor to create a new node 

    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None


def maxDepth(node):
    if node is None:
        return 0
    else:

        # Compute the depth of each subtree

        leftDepth = maxDepth(node.left)
        rightDepth = maxDepth(node.right)

        # Use the larger one
        if (leftDepth > rightDepth):
            return leftDepth + 1
        
        else:
            return rightDepth + 1
        
        # Driver code to test the above function

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)


print ("Height of tree is %d" %(maxDepth(root)))

        