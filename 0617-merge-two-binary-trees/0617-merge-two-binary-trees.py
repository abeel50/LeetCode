# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        newRoot = None
        
        def rec(newRoot, root1, root2):
            if root1 is None and root2 is None:
                return None
            newRoot = TreeNode()
            if root1:
                newRoot.val += root1.val
            if root2:
                newRoot.val += root2.val
            newRoot.left = rec(newRoot.left, root1.left if root1 else None, root2.left if root2 else None)
            newRoot.right = rec(newRoot.right, root1.right if root1 else None, root2.right if root2 else None)
            return newRoot
        newRoot = rec(newRoot, root1, root2)
        return newRoot        
            