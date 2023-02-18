# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.res = None
        
        def rec(node):
            if not node: return
            
            left = rec(node.left)
            right = rec(node.right)
            
            cur = node == p or node == q
            
            if (left and right) or (cur and right) or (cur and left):
                self.res = node
                return
            return left or right or cur
        
        rec(root)
        return self.res
        
        