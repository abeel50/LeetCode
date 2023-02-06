# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def rec(root):
            if not root: return
            l = rec(root.left)
            r = rec(root.right)
            
            if root.val == 2:
                return l or r
            if root.val == 3:
                return l and r
            else:
                return root.val
        return rec(root)