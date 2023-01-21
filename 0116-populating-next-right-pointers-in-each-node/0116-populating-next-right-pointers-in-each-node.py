"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        #recursive function
        def rec(root):
            if not root: return
            
            # check if it's leaf node
            if root.left and root.right:
                
                #connects left--> right
                root.left.next = root.right

                #left and right nodes
                left, right = root.left, root.right
                
                # to connect left side's rightmost node to right side's leftmoste
                if left.right and right.left:
                    temp = left
                    while temp.next:
                        temp.right.next = temp.next.left
                        temp = temp.next
                
                rec(root.left)
                rec(root.right)
            return
        rec(root)
        return root
        
        
        