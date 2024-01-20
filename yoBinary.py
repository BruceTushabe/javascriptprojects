class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node
        
def maxDepth(node):
    if node is None:
        return 0
    
    else:
        # Compute depth of each subtree

        leftDepth = maxDepth(node.left)
        rightDepth = maxDepth(node.right)

        # Use the larger one

        if (leftDepth > rightDepth):
            return leftDepth + 1
        else:
            return rightDepth + 1
        
# Driver code to test the above code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of the tree %d" % (maxDepth(root)))
