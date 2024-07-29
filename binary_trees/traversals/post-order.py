class Node :
    def __init__(self, val) :
        self.val = val
        self.left = None
        self.right = None

class BST :
    def __init__(self) :
        self.post_order = []

    def post_order (self, root) :
        # Base case
        if (root == None) :
            return 
        
        # Left
        self.post_order(root.left) 

        # Right
        self.post_order(root.right) 

        # Add
        self.post_order.append(root.val)