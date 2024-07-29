class Node :
    def __init__(self, val) :
        self.val = val
        self.left = None
        self.right = None

class BST :
    def __init__(self) :
        self.pre_order = []

    def pre_order (self, root) :
        # Base case
        if (root == None) :
            return 
        
        # Add
        self.pre_order.append(root.val)
        
        # Left
        self.pre_order(root.left) 

        # Right
        self.pre_order(root.right) 

        