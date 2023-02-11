"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def rec(root):
            if not root: return 0
            if not root.children: return 1
            
            return max([1 + rec(c) for c in root.children])
               
        return rec(root)
        