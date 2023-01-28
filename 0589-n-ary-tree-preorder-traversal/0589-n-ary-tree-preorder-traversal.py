"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        res =[]
        
        def helper(node):
            if not node : return
            res.append(node.val)
            if node.children is not None:
                for i in node.children:
                    helper(i)
            return
        helper(root)
        return res
        