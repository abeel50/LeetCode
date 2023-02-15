"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        
        def rec(root,level):
            if not root: return
            
            if level <= len(res):
                res[level-1].append(root.val)
            else:
                res.append([root.val])
            
            for c in root.children:
                rec(c, level + 1)
                
        rec(root, 1)
        return res
            
        