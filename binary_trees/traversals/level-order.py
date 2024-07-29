from collections import deque

class Node :
    def __init__(self, val) :
        self.val = val
        self.left = None
        self.right = None

class BST :
    def level_order (self, root) :
        # Variables
        result = []
        queue = deque()

        queue.appendleft(root)

        while (len(queue) > 0) :
            # Get level
            size = len(queue)
            level = []

            for i in range(size) :
                # Pop
                curr = queue.pop()

                # Add
                level.append(curr.val)

                # Add children
                if (curr.left != None) :
                    queue.appendleft(curr.left)
                if (curr.right != None) :
                    queue.appendleft(curr.right)
                
            result.append(level)

        return result
                