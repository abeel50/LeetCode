# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def rec(root):
            if not root: return None
            
            left, right = root.left, root.right
            
            root.left, root.right = right, left
            
            root.left = rec(root.left)
            root.right = rec(root.right)
            return root
        return rec(root)
        