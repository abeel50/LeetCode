# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def rec(root):
            if not root:
                return -1
            nonlocal res
            left, right = rec(root.left), rec(root.right)
            res = max(res, 2 + left + right)
            return 1 + max(left, right)
        rec(root)
        return res