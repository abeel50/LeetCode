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
        
        def rec(root):
            if not root: return
            if root.left and root.right:
                root.left.next = root.right

                left, right = root.left, root.right
                
                if left and left.right and right and right.left:
                    temp = left
                    while temp.next:
                        temp.right.next = temp.next.left
                        temp = temp.next
                rec(root.left)
                rec(root.right)
        rec(root)
        return root
        
        
        