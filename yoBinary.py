class Node:
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None

# Utility function to create a new node
        
def newNode(node):

    temp = Node()
    temp.key = node
    temp.left, temp.right = None, None
    return temp

# Function to find the height(depth) of the tree
def height(root):
    depth = 0

    q = []

    # Appending first level element along with None

    q.append(root)
    q.append(None)

    while (len(q) > 0):
        temp = q[0]
        q = q[1:]

        #When None encountered, incrementthe value
        if(temp == None):
            depth += 1

        # If None not encountered, keep moving
        if(temp != None):
            if(temp.left):
                q.append(temp.left)

            if(temp.right):
                q.append(temp.right)

    # If queue still have elements left,
        # append None again to the queue.
                
        elif(len(q) > 0):
            q.append(None)

    return depth

# Driver program
# Let us create Binary Tree shown in above example

root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)

print(f"Height(Depth) of tree is: {height(root)}")







