class Node :
    def __init__(self, val) :
        self.val = val
        self.left = None
        self.right = None

class BST :
    def __init__(self) :
        self.in_order = []

    def in_order (self, root) :
        # Base case
        if (root == None) :
            return 
        
        # Left
        self.in_order(root.left) 

        # Add
        self.in_order.append(root.val)

        # Right
        self.in_order(root.right) 

        